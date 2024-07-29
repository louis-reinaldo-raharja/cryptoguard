import streamlit as st
from fetch_coin_api import get_historical_prices, get_benchmark_data
from detect_anomalies import detect_anomalies
from detect_volatilities import calculate_historical_volatility, detect_volatility_spikes
from visualisation import *
from onchain_analysis import *
from scam_content import *
from how_to_use_content import *
from llm_utils import *

def learning_path_page():
    st.title("Cryptocurrency Learning Assistant")
    
    # Load learning paths from document.json
    learning_paths = load_learning_paths()
    
    # Course level selection
    course_level = st.selectbox("Select your course level:", list(learning_paths.keys()))
    
    # Reset progress when changing course level
    if 'current_course' not in st.session_state or st.session_state.current_course != course_level:
        st.session_state.progress = 0
        st.session_state.current_course = course_level
    
    # Get user's progress
    progress = st.session_state.get('progress', 0)
    
    # Display current topic
    current_topic = learning_paths[course_level][progress]['topic']
    current_question = learning_paths[course_level][progress]['question']
    current_text = learning_paths[course_level][progress]['text']
    
    st.subheader(f"Current Topic: {current_topic}")
    st.write(f"Question: {current_question}")
    
    # Display the answer
    st.write("Answer:")
    st.write(current_text)
    
    # User input for follow-up questions
    user_question = st.text_input("Ask a follow-up question about this topic:", value=current_question)
    
    if st.button("Answer"):
        if user_question:
            response = rag(user_question, course_level)
            st.write("Follow-up Answer:")
            st.write(response)
    
    # Next topic button
    st.subheader("What's Next?")
    if progress < len(learning_paths[course_level]) - 1:
        next_topic = learning_paths[course_level][progress + 1]['topic']
        if st.button(f"Move to next topic: {next_topic}"):
            st.session_state.progress = progress + 1
            st.rerun()
    else:
        st.write("Congratulations! You've completed this course level.")
        if st.button("Restart the course"):
            st.session_state.progress = 0
            st.rerun()
    
    # Display progress
    st.progress((progress + 1) / len(learning_paths[course_level]))
    st.write(f"Progress: {progress + 1}/{len(learning_paths[course_level])} topics completed")

def anomaly_detection_page():
    st.title("Cryptocurrency Anomaly and Volatility Analysis 📈💰📊")
    
    base_options = ["BTC", "ETH", "SOL", "LINK", "USDT", "BNB", "XRP", "DOGE", "ADA", "AVAX", "AAVE", "SHIB", "DOT", "NEAR", "DAI", "LTC", "BCH", "MATIC", "PEPE", "UNI", "ARB", "FLOKI"]
    quote_options = ["USDT", "USD", "USDC", "ETH", "BTC"]
    exchange_options = ["BINANCE", "COINBASE", "KRAKEN", "BITSTAMP", "GEMINI"]
    
    base = st.selectbox("Select base currency", base_options)
    quote = st.selectbox("Select quote currency", quote_options)
    exchange = st.selectbox("Select your exchange", exchange_options)
    
    benchmark_exchanges = st.multiselect(
        "Select exchanges for benchmark data",
        exchange_options,
        ["BINANCE", "COINBASE", "KRAKEN"]
    )
    
    if st.button("Analyze"):
        try:
            with st.spinner("Fetching data..."):
                data = get_historical_prices(base, quote, exchange)
                benchmark_data = get_benchmark_data(base, quote, benchmark_exchanges)
            
            result = detect_anomalies(data, benchmark_data)
            result = calculate_historical_volatility(result)
            result = detect_volatility_spikes(result)
            
            st.subheader("Price Comparison and Anomalies")
            fig_prices = plot_prices_and_anomalies(result, base, quote)
            st.plotly_chart(fig_prices)
            
            st.subheader("Historical Volatility")
            fig_volatility = plot_volatility(result, base, quote)
            st.plotly_chart(fig_volatility)
            
            st.subheader("Price Data, Anomalies, and Volatility")
            price_table = display_price_table(result)
            st.dataframe(price_table)
            
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


def onchain_analysis_page():
    st.title("On-Chain Data Analysis ⛓")

    st.header("1. Large Transaction Monitor")
    
    threshold = st.number_input("Enter transaction threshold (in ETH)", min_value=1.0, value=100.0)
    
    if st.button("Fetch Large Transactions"):
        large_txs = fetch_large_transactions(threshold)
        
        if not large_txs.empty:
            st.dataframe(large_txs)
            
            fig = create_large_transactions_chart(large_txs)
            st.plotly_chart(fig)
        else:
            st.write("No large transactions found.")

    st.header("2. Wallet Movement Tracker")
    
    wallet_address = st.text_input("Enter wallet address to track")
    
    if st.button("Track Wallet Movements"):
        wallet_txs = fetch_wallet_transactions(wallet_address)
        
        if not wallet_txs.empty:
            st.dataframe(wallet_txs)
            
            fig = create_wallet_transactions_chart(wallet_txs)
            st.plotly_chart(fig)
        else:
            st.write("No transactions found for this wallet.")

def sentiments_and_hype_page():
    st.title("Cryptocurrency Sentiments and Hype Analyzer")

    user_query = st.text_input("Enter a cryptocurrency name or topic:")

    if user_query:
        # Get real-time data from You.com
        you_response = get_ai_snippets_for_query(user_query)
        
        # Generate response using LangChain and OpenAI
        qa_chain = setup_qa_chain()
        response = qa_chain.invoke(user_query)
        
        # Analyze sentiment and hype
        web_results = [hit['snippets'] for hit in you_response.get('hits', [])]
        sentiment_hype_analysis = analyze_sentiment_and_hype(user_query, web_results)
        
        # Parse sentiment and hype scores
        sentiment_score = int(sentiment_hype_analysis.split('\n')[0].split(':')[1].strip())
        hype_score = int(sentiment_hype_analysis.split('\n')[1].split(':')[1].strip())
        analysis = sentiment_hype_analysis.split('\n')[2].split(':')[1].strip()
        
        # Display results
        st.write(f"TLDR of {user_query}:")
        st.write(response["result"])
        st.write(analysis)

        
        # Display sentiment and hype gauge charts
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(create_gauge(sentiment_score, "Sentiment"), use_container_width=True)
        with col2:
            st.plotly_chart(create_gauge(hype_score, "Hype"), use_container_width=True)
        
        
        # Display news results as a table
        news_response = get_news_for_query(user_query)
        st.write("News Results:")
        news_data = []

        for result in news_response.get('news', {}).get('results', []):
            news_data.append({
                "Title": result.get('title', 'N/A'),
                "Description": result.get('description', 'N/A')[:100] + '...',
                "URL": result.get('url', 'N/A')
            })
        
        news_df = pd.DataFrame(news_data)
        st.table(news_df)

def crypto_recommendations_page():
    st.title("Cryptocurrency Investment Recommendations")

    # User inputs
    age = st.slider("Your Age", 18, 100, 30)
    risk_appetite = st.select_slider("Risk Appetite", options=["Low", "Medium", "High"])
    knowledge_level = st.select_slider("Cryptocurrency Knowledge Level", options=["Beginner", "Intermediate", "Advanced"])
    emergency_fund = st.number_input("Emergency Fund (in months of expenses)", min_value=0, max_value=36, value=3)
    investment_percentage = st.slider("Percentage of Savings to Invest", 0, 100, 10)
    other_investments = st.multiselect(
        "Other Investments",
        ["Stocks", "Bonds", "Real Estate", "Mutual Funds", "ETFs", "Commodities", "Forex", "None"],
        default=["None"]
    )

    if st.button("Get Recommendations"):
        # Get recommendations
        recommendations = get_crypto_recommendations(age, risk_appetite, knowledge_level, emergency_fund, investment_percentage, other_investments)
        
        # Display overall recommendation
        st.write("Overall Recommendation:")
        st.write(recommendations["overall_recommendation"])
        
        # Display coin recommendations as a table
        if recommendations["coin_recommendations"]["coins"]:
            st.write("Recommended Cryptocurrencies:")
            df = pd.DataFrame(recommendations["coin_recommendations"]["coins"])
            st.table(df)
        
        # Display risk warning
        st.write("Risk Warning:")
        st.write(recommendations["risk_warning"])

        # Add a disclaimer
        st.sidebar.warning("Disclaimer: This tool provides general recommendations for educational purposes only. Always do your own research and consult with a financial advisor before making investment decisions.")

def main():
    st.logo("images/logo.png")
    st.sidebar.title("CryptoGuard")
    page = st.sidebar.radio("Go to", ["0.How to Use", "1.Anomaly Detection", "2.On-Chain Analysis", "3.Common Scams", "4.Hype and Sentiment", "5.Crypto Recommendations", "6.Learning Path"])

    if page == "0.How to Use":
        how_to_use_page()
    elif page == "1.Anomaly Detection":
        anomaly_detection_page()
    elif page == "2.On-Chain Analysis":
        onchain_analysis_page()
    elif page == "3.Common Scams":
        scam_types_page()
    elif page == "4.Hype and Sentiment":
        sentiments_and_hype_page()
    elif page == "5.Crypto Recommendations":
        crypto_recommendations_page()
    elif page == "6.Learning Path":
        learning_path_page()

if __name__ == "__main__":
    main()