import numpy as np

def calculate_historical_volatility(data, window=20):
    data['returns'] = data['price_close'].pct_change()
    data['volatility'] = data['returns'].rolling(window=window).std() * np.sqrt(252)
    return data

def detect_volatility_spikes(data, threshold=2):
    vol_mean = data['volatility'].mean()
    vol_std = data['volatility'].std()
    data['volatility_spike'] = data['volatility'] > (vol_mean + threshold * vol_std)
    return data
