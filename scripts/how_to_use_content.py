import streamlit as st

def how_to_use_page():
    st.title("Welcome to CryptoGuard")

    st.write("""
    CryptoGuard is a comprehensive cryptocurrency monitoring and education platform designed to help you navigate the complex world of digital assets safely and intelligently.
    """)

    st.header("Features Overview")

    st.subheader("1. Anomaly Detection")
    st.write("""
    Our advanced anomaly detection system monitors cryptocurrency markets in real-time, identifying unusual patterns that may indicate potential fraud or market manipulation.
    
    How to use:
    - Select your base and quote currencies
    - Choose your exchange and benchmark exchanges
    - Analyze price comparisons, anomalies, and historical volatility
    - Pay attention to sudden price spikes, drops, or volume anomalies
    """)

    st.subheader("2. On-Chain Analysis")
    st.write("""
    Dive deep into blockchain data to detect suspicious activities and track large transactions.
    
    How to use:
    - Monitor large transactions above a specified threshold
    - Track wallet movements for specific addresses
    - Identify potential wash trading or other suspicious patterns
    """)

    st.subheader("3. Common Scams Education")
    st.write("""
    Learn about prevalent cryptocurrency scams to protect yourself from fraud.
    
    How to use:
    - Explore detailed information on various scam types (e.g., Ponzi schemes, pump and dump)
    - Read real victim stories and estimated losses
    - Access resources to learn more about each scam type
    """)

    st.subheader("4. Hype and Sentiment Analysis")
    st.write("""
    Gauge market sentiment and hype levels for specific cryptocurrencies.
    
    How to use:
    - Enter a cryptocurrency name or topic
    - View sentiment and hype scores
    - Read AI-generated analysis and relevant news
    """)

    st.subheader("5. Crypto Recommendations")
    st.write("""
    Receive personalized cryptocurrency investment recommendations based on your profile.
    
    How to use:
    - Input your age, risk appetite, knowledge level, and financial situation
    - Get tailored recommendations and risk warnings
    - View suggested cryptocurrencies or alternative investments
    """)

    st.subheader("6. Learning Path")
    st.write("""
    Enhance your cryptocurrency knowledge with our interactive learning modules.
    
    How to use:
    - Select your course level (Beginner, Intermediate, Advanced)
    - Progress through topics and answer questions
    - Ask follow-up questions to deepen your understanding
    """)

    st.header("Getting Started")
    st.write("""
    If you're new to cryptocurrencies or CryptoGuard, we recommend the following path:

    1. Start with the Learning Path:
       - Begin with the Beginner course level
       - Complete all topics to build a strong foundation

    2. Explore Common Scams:
       - Familiarize yourself with different types of cryptocurrency scams
       - Learn how to identify and avoid potential fraud

    3. Use the Crypto Recommendations:
       - Input your personal information to get tailored advice
       - Understand your risk profile and suitable investment options

    4. Practice with Anomaly Detection:
       - Start monitoring well-known cryptocurrencies
       - Learn to identify unusual patterns and potential red flags

    5. Dive into On-Chain Analysis:
       - Begin tracking large transactions and wallet movements
       - Develop skills in identifying suspicious blockchain activities

    6. Utilize Hype and Sentiment Analysis:
       - Research cryptocurrencies you're interested in
       - Learn to balance hype with fundamental analysis

    Remember, cryptocurrency investments carry high risk. Always do your own research and never invest more than you can afford to lose.
    """)