import streamlit as st

def how_to_use_page():
    st.title("Understanding Crypto Market Analysis")

    st.write("""
    This page provides an overview of the different analysis techniques used in our app to detect potential anomalies and red flags in the cryptocurrency market.
    """)

    st.header("1. Anomaly Detection")
    st.subheader("Methodology")
    st.write("""
    Anomaly detection in cryptocurrency markets involves identifying unusual patterns or events that deviate significantly from the expected behavior. We use statistical methods to detect these anomalies:

    1. Calculate the mean and standard deviation of price movements for your chosen exchange.
    2. Obtain similar data from regulated centralized exchanges to use as a benchmark.
    3. Compare the price movements and patterns between your exchange and the benchmark exchanges.
    4. Identify data points that fall outside a certain number of standard deviations (typically 2 or 3) from the mean.
    5. Flag these points as potential anomalies, especially if they don't align with movements in the benchmark exchanges.
    """)
    
    st.subheader("How to Use")
    st.write("""
    - Look for sudden, unexplained price spikes or drops.
    - Pay attention to anomalies that coincide with other unusual market activities.
    - Investigate the causes behind persistent anomalies.

    Red Flags:
    - Frequent anomalies without clear fundamental reasons
    - Anomalies that occur simultaneously across multiple exchanges
    """)

    st.header("2. Volatility Analysis")
    st.subheader("Methodology")
    st.write("""
    Volatility analysis measures the degree of variation in trading prices over time. We typically use metrics like:

    1. Standard Deviation of Returns
    2. Average True Range (ATR)
    3. Bollinger Bands
    """)
    
    st.subheader("How to Use")
    st.write("""
    - Compare current volatility levels to historical averages.
    - Look for periods of unusually high or low volatility.
    - Analyze how volatility changes before and after significant events.

    Red Flags:
    - Sudden spikes in volatility without clear catalysts
    - Prolonged periods of extremely low volatility (potential calm before the storm)
    """)

    st.header("3. Volume Analysis")
    st.subheader("Methodology")
    st.write("""
    Volume analysis examines the number of units traded in a given time period. We look at:

    1. Trading Volume
    2. Volume-Weighted Average Price (VWAP)
    3. On-Balance Volume (OBV)
    """)
    
    st.subheader("How to Use")
    st.write("""
    - Compare current volume to historical averages.
    - Look for volume spikes or unusual patterns.
    - Analyze the relationship between volume and price movements.

    Red Flags:
    - High price movement with low volume (potential manipulation)
    - Sudden volume spikes without corresponding news or events
    - Consistently decreasing volume in a rising market (potential weakness)
    """)

    st.header("4. On-Chain Analysis")
    st.subheader("Methodology")
    st.write("""
    On-chain analysis involves examining data directly from the blockchain. We focus on:

    1. Large Transactions
    2. Wallet Movements
    """)
    
    st.subheader("How to Use")
    st.write("""
    - Monitor large transactions for potential whale activity.
    - Track movements of known wallets (e.g., exchange wallets, large holders).

    Red Flags:
    - Unusually large transactions before significant price movements
    - Suspicious patterns in wallet movements (e.g., wash trading)
    """)

    st.header("Putting It All Together")
    st.write("""
    To effectively identify potential anomalies or red flags:

    1. Don't rely on a single indicator - look for convergence across multiple analysis techniques.
    2. Consider the broader context, including news, market sentiment, and macroeconomic factors.
    3. Be aware that not all anomalies indicate malicious activity - always investigate further before drawing conclusions.
    4. Use these tools as a starting point for deeper research and due diligence.

    Remember, while these techniques can help identify potential issues, they are not foolproof. Always conduct thorough research and consider seeking advice from financial professionals before making investment decisions.
    """)