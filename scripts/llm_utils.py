from langchain.retrievers.you import YouRetriever
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from openai import OpenAI
import json
import os
import requests
import minsearch

os.environ["YDC_API_KEY"] = "bf95c2d7-2c5e-436e-a1dc-c6e731ffc363<__>1PZRhQETU8N2v5f4LMRv2Gvo"
os.environ["OPENAI_API_KEY"] = "sk-proj-iCmaweh8buw0kgfVTp1fT3BlbkFJL4Jkr98evkzyfPcszjSw"


def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": os.getenv("YDC_API_KEY")}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()

def get_news_for_query(query):
    headers = {"X-API-Key": os.getenv("YDC_API_KEY")}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/news?q={query}",
        params=params,
        headers=headers,
    ).json()

def setup_qa_chain():
    yr = YouRetriever()
    model = "gpt-3.5-turbo-16k"
    return RetrievalQA.from_chain_type(llm=ChatOpenAI(model=model), chain_type="stuff", retriever=yr)

def analyze_sentiment_and_hype(query, web_results):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
    Analyze the sentiment and hype for the cryptocurrency "{query}" based on the following web results:

    {web_results}

    Provide a score for both sentiment and hype on a scale of 1-100, where 1 is extremely negative/low and 100 is extremely positive/high.
    Return your response in the following format:
    Sentiment: [score]
    Hype: [score]
    Analysis: [brief explanation of your scoring]
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cryptocurrency analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def get_crypto_recommendations(age, risk_appetite, knowledge_level, emergency_fund, investment_percentage, other_investments):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
    As a cryptocurrency analyst, provide investment advice for a new investor with the following profile:
    Age: {age}
    Risk Appetite: {risk_appetite}
    Knowledge Level: {knowledge_level}
    Emergency Fund: {emergency_fund} months of expenses
    Percentage of Savings to Invest: {investment_percentage}%
    Other Investments: {', '.join(other_investments)}

    Based on this profile, provide advice in the following format:
    1. Overall recommendation (invest in crypto or not, and why)
    2. If recommending crypto, suggest 3 cryptocurrencies in a dictionary format with the following structure:
       {{
           "coins": [
               {{
                   "name": "Coin Name",
                   "use_cases": "Brief description of use cases",
                   "risk_level": "Low/Medium/High",
                   "market_cap": "Approximate market cap",
                   "historical_returns_yoy": "year on year average returns in %"
                   "ranking in coinmarketcap": "Ranking"
               }},
               // ... (repeat for each recommended coin)
           ]
       }}
    3. Risk warning and allocation advice

    Consider the following guidelines:
    - If the user is inexperienced, has less than 6 months of emergency funds, does not invest in anything else, or plans to invest everything, warn against crypto and recommend safer alternatives like S&P 500 ETFs like VOO, world inex like VWRA or dividends like VIX.
    - For investors who may not be experienced with crypto, too young, no emergency fund, no other investments, instead of giving coin names in the json response, give ETFs that track the US SP500 index like V00 or a world index or dividends ETFs like VIX.
    - For users with some savings and looking to diversify, recommend top cryptocurrencies, preferably in the top 10 from coinmarketcap.
    - For experienced investors or if they have more than 6 months emergency fund and have other investments,  suggest up-and-coming coins with high potential but higher risk.
    - Always remind about the speculative nature of cryptocurrencies and recommend allocating only a small percentage of investments.
    - Can recommend broad market index fund ETFs like VOO, VWRA or VIX (for dividends) especially for low risk appetite users as it is still important to invest. 
    - If they do not have an emergency fund, encourage them to save up first to at least cover 6 months of expenses.

    Return your response as a JSON string with the following structure:
    {{
        "overall_recommendation": "Your overall recommendation text",
        "coin_recommendations": {{
            "coins": [
                // ... (coin dictionaries as described above)
            ]
        }},
        "risk_warning": "Your risk warning and allocation advice"
    }}

    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cryptocurrency analyst helping new investors make responsible financial decisions."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return json.loads(response.choices[0].message.content)

# Load documents
with open('document.json', 'rt') as f_in:
    docs_raw = json.load(f_in)

documents = []
for course_dict in docs_raw:
    for doc in course_dict['documents']:
        doc['course'] = course_dict['course']
        documents.append(doc)

# Create and fit the index
index = minsearch.Index(
    text_fields=["question", "text", "section"],
    keyword_fields=["course"]
)
index.fit(documents)

def search(query, course_level):
    boost = {'question': 3.0, 'section': 0.5}

    results = index.search(
        query=query,
        filter_dict={'course': course_level},
        boost_dict=boost,
        num_results=5
    )

    # Calculate a simple confidence score based on the relevance of the top result
    confidence = results[0]['_score'] if results else 0

    return results, confidence


def build_prompt(query, search_results):
    prompt_template = """
You are a course instructor for Crytocurrencies. Answer the QUESTION based on the CONTEXT from the document database to a 5 year old.
Use only the facts from the CONTEXT when answering the QUESTION. 

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = ""
    
    for doc in search_results:
        context = context + f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def build_web_prompt(query, web_results):
    prompt_template = """
You are a course instructor for Cryptocurrencies. Answer the QUESTION based on the CONTEXT from web search results. Use only the facts from the CONTEXT when answering the QUESTION. If the information is not directly related to cryptocurrencies, adapt it to the context of cryptocurrencies.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

    context = ""
    if isinstance(web_results, list):
        for result in web_results[:3]:  # Use top 3 results
            if isinstance(result, dict) and 'title' in result and 'snippet' in result:
                context += f"Title: {result['title']}\nSnippet: {result['snippet']}\n\n"
    elif isinstance(web_results, dict):
        for i, (title, snippet) in enumerate(zip(web_results.get('titles', []), web_results.get('snippets', [])), 1):
            if i > 3:  # Limit to top 3 results
                break
            context += f"Title: {title}\nSnippet: {snippet}\n\n"

    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt



def llm(prompt, course_level):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    content = "You are a cryptocurrency course instructor."

    if course_level == 'beginner':
        content = content + " Explain the concepts to a 5 year old."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cryptocurrency analyst." + content},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def rag(query, course_level):
    search_results, confidence = search(query, course_level)
    
    # Set a threshold for when to use web search (adjust as needed)
    confidence_threshold = 1.5

    if confidence < confidence_threshold:
        # Use web search
        print('Getting results from the web')
        web_results = get_ai_snippets_for_query(query)
        prompt = build_web_prompt(query, web_results)
    else:
        # Use local search results
        prompt = build_prompt(query, search_results)

    answer = llm(prompt, course_level)
    return answer

    
def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": os.getenv("YDC_API_KEY")}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()

