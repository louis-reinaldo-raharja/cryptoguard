import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

API_KEY = 'F8BA3BC7-53F3-436C-91CF-DBAB02A3A501'

def get_historical_prices(base, quote, exchange_id=None, period_id='5MIN', days=1):

    
    url = f'https://rest.coinapi.io/v1/ohlcv/{exchange_id}_SPOT_{base}_{quote}/history'
    
    headers = {'X-CoinAPI-Key': API_KEY}
    time_start = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat(timespec='seconds')
    
    params = {
        'period_id': period_id,
        'time_start': time_start,
        'limit': 10000  # Adjust as needed
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

def get_benchmark_data(base, quote, exchanges, period_id='5MIN', days=1):
    benchmark_data = []
    for exchange in exchanges:
        try:
            data = get_historical_prices(base, quote, exchange, period_id, days)
            data['exchange'] = exchange
            benchmark_data.append(data)
        except Exception as e:
            st.warning(f"Failed to fetch data for {exchange}: {str(e)}")
    
    if not benchmark_data:
        raise Exception("Failed to fetch benchmark data from any exchange")
    
    combined_data = pd.concat(benchmark_data)
    return combined_data.groupby('time_period_start').agg({
        'price_open': 'mean',
        'price_high': 'mean',
        'price_low': 'mean',
        'price_close': 'mean',
        'volume_traded': 'sum'
    }).reset_index()
