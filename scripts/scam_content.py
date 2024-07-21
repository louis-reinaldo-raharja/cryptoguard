import streamlit as st

def scam_types_page():
    st.title("Cryptocurrency Scam Education Dashboard")

    scams = [
        ("Ponzi Schemes", "🔄"),
        ("Pump and Dump", "📈"),
        ("Pig Butchering Scams", "🐷"),
        ("FTX Scandal", "💥")
    ]

    col1, col2 = st.columns(2)

    for i, (scam, emoji) in enumerate(scams):
        if i % 2 == 0:
            col = col1
        else:
            col = col2
        
        if col.button(f"{emoji} {scam}"):
            display_scam_details(scam)

def display_scam_details(scam):
    st.title(scam)
    
    if scam == "Ponzi Schemes":
        st.header("How it works")
        st.write("Ponzi schemes in cryptocurrency promise high returns but use new investors' funds to pay earlier investors.")
        
        st.header("Example")
        st.write("BitConnect was a well-known Ponzi scheme in the crypto world.")
        
        st.header("Estimated Losses")
        st.write("Victims lost approximately \$3.45 billion to the BitConnect scam.")
        
        st.header("Real Victim Stories")
        st.write("John, a software engineer, lost \$200,000 in the BitConnect scam.")
        st.markdown("[Read more about BitConnect victims' stories](https://www.coindesk.com/markets/2018/01/17/bitconnect-investors-left-in-limbo-as-token-price-drops-90/)")
        
        st.header("Learn More")
        st.markdown("- [Department of Justice Press Release](https://www.justice.gov/usao-sdny/pr/bitconnect-founder-indicted-global-345-billion-cryptocurrency-scheme)")
        st.markdown("- [YouTube: BitConnect - The \$2 Billion Crypto Scam](https://www.youtube.com/watch?v=lCcwn6bGUtU)")
        st.markdown("- [Reddit: BitConnect Victim Support Thread](https://www.reddit.com/r/BitcoinMarkets/comments/7qoyvv/bitconnect_shutting_down/)")
        st.markdown("- [Twitter Thread on BitConnect Collapse](https://twitter.com/cryptowhale/status/1351248104561496065)")

    elif scam == "Pump and Dump":
        st.header("How it works")
        st.write("In the crypto world, 'pump and dump' schemes involve artificially inflating the price of a cryptocurrency. Influencers or individuals with a large following often promote a coin, leading to a rapid price increase ('pump').  Once the price peaks, these insiders sell their holdings ('dump'), causing a sharp decline and leaving unsuspecting investors with losses.") 
        
        st.header("Examples")
        st.write("- **Boogie2988:**  In 2020, YouTuber Boogie2988 promoted a cryptocurrency called 'DLive' shortly before its price crashed. Many accused him of participating in a pump and dump scheme, though he denied these allegations.")
        st.write("- **Logan Paul:** Logan Paul faced criticism for his promotion of various cryptocurrency projects, including 'Dink Doink' and 'CryptoZoo.' These projects were accused of being pump and dumps, resulting in significant losses for some investors.") 
        
        st.header("Estimated Losses")
        st.write("While precise figures are difficult to calculate, pump and dump schemes can lead to millions of dollars in losses for unsuspecting investors. The volatile nature of cryptocurrencies makes them particularly susceptible to this type of manipulation.")
        
        st.header("Red Flags to Look Out For")
        st.write("1. **Sudden, aggressive promotion:** Be wary of coins heavily promoted by celebrities or influencers, especially if the promotion lacks substance or due diligence.")
        st.write("2. **Unrealistic promises:**  Promises of guaranteed or extremely high returns are often a red flag.  ")
        st.write("3. **Lack of real-world utility:** Investigate whether the cryptocurrency has a genuine purpose or use case beyond speculation.")
        st.write("4. **Artificial hype:** Be cautious of projects that rely heavily on hype, celebrity endorsements, or social media trends to drive up prices.")
        st.write("5. **FOMO (Fear Of Missing Out):** Avoid making impulsive decisions based on pressure tactics or the fear of missing out on potential profits. ")

        st.header("Real Victim Stories")
        st.write("Many individuals have come forward claiming significant losses from investing in projects promoted by these celebrities.  However, due to the often-anonymous nature of cryptocurrency, concrete victim testimonies can be difficult to find.")

        st.header("Learn More")
        st.markdown("- [Article on Boogie2988 and DLive](https://www.dexerto.com/entertainment/boogie2988-responds-to-dlive-crypto-pump-and-dump-accusations-1405994/)")
        st.markdown("- [Information on Logan Paul's CryptoZoo controversy](https://www.sportskeeda.com/esports/news-logan-paul-cryptozoo-controversy-explained-youtuber-accused-allegedly-scamming-millions-nft-game)")
        st.markdown("- [Coffeezilla YouTube: I Confronted The Biggest Crypto Scammer Of 2021](https://www.youtube.com/watch?v=uBTCxP2uTxY)") 
        st.markdown("- [Coffeezilla YouTube: This YouTuber SCAMMED His Fans (For \$5,000,000)](https://www.youtube.com/watch?v=380nKpoIges)") 

    elif scam == "Pig Butchering Scams":
        st.header("How it works")
        st.write("Scammers build trust with victims over time, often through romantic relationships, before convincing them to invest in fake cryptocurrency schemes.")
        
        st.header("Example")
        st.write("A man lost \$1 million after initial contact with a scammer pretending to be an old colleague on WhatsApp.")
        
        st.header("Estimated Losses")
        st.write("More than \$75 billion was lost to pig butchering scams from 2020 to 2024.")
        
        st.header("Real Victim Stories")
        st.write("Emily, a marketing executive, lost \$300,000 after being convinced to invest by someone she met on a dating app.")
        st.markdown("[Read Emily's story and other pig butchering scam accounts](https://www.cnbc.com/2022/10/08/pig-butchering-crypto-scam-cost-one-man-millions.html)")
        
        st.header("Learn More")
        st.markdown("- [CNBC: 'Pig butchering' crypto scams cost investors millions](https://www.cnbc.com/2022/10/08/pig-butchering-crypto-scam-cost-one-man-millions.html)")
        st.markdown("- [YouTube: Anatomy of a Pig Butchering Scam](https://www.youtube.com/watch?v=RVd3PL6qYKA)")
        st.markdown("- [Reddit: Pig Butchering Scam Awareness Thread](https://www.reddit.com/r/Scams/comments/na8oax/asian_guygirl_from_online_dating_mentors_you_to/)")
        st.markdown("- [Twitter: FBI Warning on Pig Butchering Scams](https://twitter.com/FBI/status/1587115052829224960)")

    elif scam == "FTX Scandal":
        st.header("How it happened")
        st.write("FTX, once a major cryptocurrency exchange, collapsed due to misuse of customer funds and lack of proper oversight. The scandal involved:")
        st.write("- Misappropriation of billions in customer deposits for unauthorized purposes")
        st.write("- Using customer funds to prop up Alameda Research, a trading firm also owned by Sam Bankman-Fried")
        st.write("- Creating a 'backdoor' in FTX's systems to move funds without triggering internal compliance or accounting red flags")
        st.write("- Providing large personal loans to FTX executives")
        st.write("- Misleading investors and the public about FTX's financial health and risk management practices")

        st.image("images/sbf.jpeg", caption="Sam Bankman-Fried, founder of FTX")
        
        st.header("Key Points")
        st.write("- Misuse of customer funds for unauthorized purposes")
        st.write("- Inadequate risk management and accounting practices")
        st.write("- Criminal charges against founder Sam Bankman-Fried")
        
        st.header("Estimated Losses")
        st.write("Approximately \$8 billion in customer funds were lost when FTX collapsed.")
        
        st.header("Real Victim Stories")
        st.write("Tom, a small business owner, lost his entire \$50,000 savings that he had invested through FTX.")
        st.markdown("[Explore personal accounts of FTX victims](https://www.theguardian.com/technology/2022/nov/19/the-money-is-gone-people-who-lost-out-in-ftxs-collapse)")

        st.header("Red Flags to Look Out For 🚩🚩🚩")
        st.write("To avoid falling victim to similar scams, watch out for these warning signs:")
        st.write("1. Lack of transparency in company operations and financials")
        st.write("2. Complex or vague explanations of business models")
        st.write("3. Excessive hype or celebrity endorsements")
        st.write("4. Lack of clear regulatory compliance or resistance to audits")
        st.write("5. Mixing of customer funds with company operations")
        
        st.header("Learn More")
        st.markdown("- [FTX Bankruptcy Information](https://cases.ra.kroll.com/FTX/)")
        st.markdown("- [YouTube: The Rise and Fall of FTX Explained](https://www.youtube.com/watch?v=Abd8L_Conow)")
        st.markdown("- [Reddit: FTX Collapse Discussion](https://www.reddit.com/r/CryptoCurrency/comments/yrs380/ftx_collapse_megathread/)")
        st.markdown("- [Twitter: Crypto Journalist's Thread on FTX Scandal](https://twitter.com/laurashin/status/1590696594643554304)")

    if st.button("Back to Scam Types"):
        st.experimental_rerun()
