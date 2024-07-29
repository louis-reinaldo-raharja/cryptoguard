import streamlit as st

def scam_types_page():
    st.title("Cryptocurrency Scam Education Dashboard")

    scams = [
        ("Ponzi Schemes", "🔄"),
        ("Pump and Dump", "📈"),
        ("Pig Butchering Scams", "🐷"),
        ("FTX Scandal", "💥"),
        ("Fake ICOs", "🎭"),
        ("Phishing Attacks", "🎣"),
        ("Rug Pulls", "🏃‍♂️"),
        ("Fake Exchanges", "🏦"),
        ("Social Media Impersonation", "👥"),
        ("Malware Wallets", "🦠"),
        ("Sandwich Attack", "🥪")
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
    
    elif scam == "Fake ICOs":
        st.header("How it works")
        st.write("Fraudsters create fake Initial Coin Offerings (ICOs) for non-existent cryptocurrency projects, promising high returns to lure investors.")
        
        st.header("Example")
        st.write("The 'PlexCoin' ICO raised \$15 million before being shut down by the SEC.")
        
        st.header("Estimated Losses")
        st.write("Fake ICOs have cost investors billions of dollars globally.")
        
        st.header("Red Flags")
        st.write("1. Unrealistic promises of high returns")
        st.write("2. Lack of a clear, viable business plan")
        st.write("3. Anonymous or unverifiable team members")
        st.write("4. Absence of a working prototype or product")
        
        st.header("Learn More")
        st.markdown("- [SEC Investor Alert on ICOs](https://www.sec.gov/oiea/investor-alerts-and-bulletins/ib_coinofferings)")
        st.markdown("- [CoinDesk: The Rise and Fall of PlexCoin](https://www.coindesk.com/markets/2017/12/04/sec-files-fraud-charges-against-plexcoin-ico-organizer/)")

    elif scam == "Phishing Attacks":
        st.header("How it works")
        st.write("Scammers create fake websites or send emails mimicking legitimate cryptocurrency services to steal users' login credentials and private keys.")
        
        st.header("Example")
        st.write("In 2018, hackers stole \$50 million worth of Ethereum using a phishing attack on the Bee Token ICO.")
        
        st.header("Estimated Losses")
        st.write("Phishing attacks in the crypto space have resulted in hundreds of millions of dollars in losses.")
        
        st.header("Red Flags")
        st.write("1. Unsolicited emails or messages asking for private keys or login information")
        st.write("2. URLs that are slightly different from legitimate websites")
        st.write("3. Pressure to act quickly or provide sensitive information")
        
        st.header("Learn More")
        st.markdown("- [Binance Academy: Crypto Phishing](https://academy.binance.com/en/articles/what-is-phishing)")
        st.markdown("- [CoinDesk: Bee Token ICO Phishing Scam](https://www.coindesk.com/markets/2018/02/01/bee-token-ico-stung-by-phishing-scam/)")

    elif scam == "Rug Pulls":
        st.header("How it works")
        st.write("Developers create a new cryptocurrency token, artificially inflate its value, then suddenly sell off their holdings, causing the price to crash.")
        
        st.header("Example")
        st.write("The AnubisDAO rug pull in 2021 resulted in \$60 million worth of investor funds being stolen.")
        
        st.header("Estimated Losses")
        st.write("Rug pulls accounted for 37% of all cryptocurrency scam revenue in 2021, totaling about \$2.8 billion.")
        
        st.header("Red Flags")
        st.write("1. Anonymous development team")
        st.write("2. Locked liquidity for a short period")
        st.write("3. Excessive hype and promises of unrealistic returns")
        st.write("4. Large portion of tokens held by a small number of wallets")
        
        st.header("Learn More")
        st.markdown("- [Chainalysis: The Biggest Threat to Trust in Cryptocurrency: Rug Pulls Put 2021 Cryptocurrency Scam Revenue Close to All-time Highs](https://blog.chainalysis.com/reports/2021-crypto-scam-revenues/)")
        st.markdown("- [CoinDesk: AnubisDAO Investors Lose \$60M in Apparent Rug Pull](https://www.coindesk.com/markets/2021/10/29/anubisdao-investors-lose-60m-in-apparent-rug-pull/)")

    elif scam == "Fake Exchanges":
        st.header("How it works")
        st.write("Scammers create fake cryptocurrency exchanges that appear legitimate but are designed to steal users' funds or personal information.")
        
        st.header("Example")
        st.write("In 2019, the IDAX exchange suddenly shut down, with the CEO reportedly going missing along with the private keys to user funds.")
        
        st.header("Estimated Losses")
        st.write("Losses from fake exchanges can range from thousands to millions of dollars per incident.")
        
        st.header("Red Flags")
        st.write("1. Unusually high trading volumes for a new or unknown exchange")
        st.write("2. Lack of regulatory compliance or licensing information")
        st.write("3. Poor website security (e.g., no HTTPS)")
        st.write("4. Limited or non-existent customer support")
        
        st.header("Learn More")
        st.markdown("- [CoinDesk: IDAX Exchange Says CEO Has Gone Missing With Cold Wallet Keys](https://www.coindesk.com/markets/2019/11/29/idax-exchange-says-ceo-has-gone-missing-with-cold-wallet-keys/)")
        st.markdown("- [Crypto.com: How to Spot a Fake Crypto Exchange](https://crypto.com/university/how-to-spot-fake-crypto-exchanges)")

    elif scam == "Social Media Impersonation":
        st.header("How it works")
        st.write("Scammers create fake social media accounts impersonating well-known figures in the crypto space or legitimate projects to trick users into sending cryptocurrency.")
        
        st.header("Example")
        st.write("In 2020, a Twitter hack compromised high-profile accounts like Elon Musk and Barack Obama to promote a Bitcoin scam.")
        
        st.header("Estimated Losses")
        st.write("The 2020 Twitter hack alone resulted in over \$100,000 worth of Bitcoin being stolen.")
        
        st.header("Red Flags")
        st.write("1. Requests to send cryptocurrency for a promised return")
        st.write("2. Urgency or time-limited offers")
        st.write("3. Slight variations in usernames or handles from official accounts")
        st.write("4. Poor grammar or spelling in posts")
        
        st.header("Learn More")
        st.markdown("- [The Verge: Twitter hack recap](https://www.theverge.com/2020/7/15/21326200/elon-musk-bill-gates-twitter-hack-bitcoin-scam-compromised)")
        st.markdown("- [FTC: How to Spot, Avoid and Report Crypto Scams](https://consumer.ftc.gov/articles/how-spot-avoid-and-report-crypto-scams)")

    elif scam == "Malware Wallets":
        st.header("How it works")
        st.write("Hackers create fake cryptocurrency wallet apps that, when installed, steal users' private keys or redirect transactions to the scammer's wallet.")
        
        st.header("Example")
        st.write("In 2021, a fake Trezor app on the Apple App Store stole \$600,000 in Bitcoin from one user.")
        
        st.header("Estimated Losses")
        st.write("Malware wallets have resulted in millions of dollars in cryptocurrency theft.")
        
        st.header("Red Flags")
        st.write("1. Wallet apps not downloaded from official sources")
        st.write("2. Apps requesting unusual permissions")
        st.write("3. Negative or suspicious reviews in app stores")
        st.write("4. Promises of unrealistic returns or mining capabilities")
        
        st.header("Learn More")
        st.markdown("- [Washington Post: He lost \$1 million to a crypto scam](https://www.washingtonpost.com/technology/2021/05/17/apple-app-store-scams-fraud/)")
        st.markdown("- [Kaspersky: Cryptocurrency Malware](https://www.kaspersky.com/resource-center/definitions/what-is-cryptocurrency-malware)")

    elif scam == "Sandwich Attack":
        st.header("How it works")
        st.write("A sandwich attack is a type of front-running attack in decentralized finance (DeFi) where an attacker places one transaction immediately before and another immediately after a victim's transaction, manipulating the price and profiting from the difference.")
        
        st.header("Example")
        st.write("In 2020, researchers found that sandwich attacks were prevalent on decentralized exchanges like Uniswap, with some attackers earning significant profits.")
        
        st.header("Estimated Losses")
        st.write("While exact figures are hard to determine, it's estimated that millions of dollars have been lost to sandwich attacks across various DeFi platforms.")
        
        st.header("Red Flags")
        st.write("1. Unexpected slippage or price impact on your trades")
        st.write("2. Transactions taking longer than usual to confirm")
        st.write("3. Unusual activity in the mempool before and after your transaction")
        st.write("4. Consistently getting worse prices than expected on DEX trades")
        
        st.header("How to Protect Yourself")
        st.write("1. Use DEXs with built-in protections against front-running")
        st.write("2. Set appropriate slippage tolerance for your trades")
        st.write("3. Consider using private transaction services or relayers")
        st.write("4. Be cautious when trading less liquid tokens or during high network congestion")
        
        st.header("Learn More")
        st.markdown("- [Consensys: Understanding Sandwich Attacks](https://consensys.net/blog/metamask/understanding-sandwich-attacks/)")
        st.markdown("- [CoinMarketCap: What Is a Sandwich Attack?](https://coinmarketcap.com/alexandria/article/what-is-a-sandwich-attack)")
        st.markdown("- [Research Paper: Quantifying Blockchain Extractable Value](https://arxiv.org/abs/2101.05511)")

    if st.button("Back to Scam Types"):
        st.rerun()
