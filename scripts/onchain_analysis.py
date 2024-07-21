from web3 import Web3
import requests
import pandas as pd
from datetime import datetime, timedelta

# Initialize Web3 connection (replace with your own Infura project ID)

# Etherscan API key (replace with your own)
INFURA_API_KEY = "f4134360edfc40dfa191ae126f5a427d"
ETHERSCAN_API_KEY = "9DWQV1PW4IRR48HZWM5HB4WU8S2II5RBVZ"

infura_url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
w3 = Web3(Web3.HTTPProvider(infura_url))

def fetch_large_transactions(threshold):
    latest_block = w3.eth.get_block('latest')
    transactions = []

    for i in range(10):  # Check the last 10 blocks
        block = w3.eth.get_block(latest_block.number - i, full_transactions=True)
        for tx in block.transactions:
            if tx['value'] > w3.to_wei(threshold, 'ether'):
                transactions.append({
                    'from': tx['from'],
                    'to': tx['to'],
                    'value': w3.from_wei(tx['value'], 'ether')
                })

    print(transactions)
    return pd.DataFrame(transactions)

def fetch_wallet_transactions(address):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=desc&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    # print(data)

    if data['status'] == '1':
        transactions = pd.DataFrame(data['result'])
        # Convert 'timeStamp' to integer before passing to to_datetime
        transactions['timeStamp'] = pd.to_datetime(transactions['timeStamp'].astype(int), unit='s')
        transactions['value'] = transactions['value'].astype(float) / 1e18  # Convert to ETH
        return transactions[['timeStamp', 'from', 'to', 'value']]
    else:
        return pd.DataFrame()