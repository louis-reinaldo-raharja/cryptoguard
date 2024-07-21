import pandas as pd
import numpy as np

def calculate_vwap(data):
    data['vwap'] = (data['price_close'] * data['volume_traded']).cumsum() / data['volume_traded'].cumsum()
    return data

def detect_price_anomalies(merged_data):
    mean_diff = merged_data['price_diff'].mean()
    std_diff = merged_data['price_diff'].std()
    
    merged_data['Price_Anomaly'] = np.where(
        (merged_data['price_diff'] > mean_diff + 2 * std_diff) | 
        (merged_data['price_diff'] < mean_diff - 2 * std_diff),
        True, False
    )
    return merged_data

def detect_volume_anomalies(merged_data):
    volume_mean = merged_data['volume_traded'].mean()
    volume_std = merged_data['volume_traded'].std()
    merged_data['Volume_Anomaly'] = np.where(
        merged_data['volume_traded'] > volume_mean + 2 * volume_std,
        True, False
    )
    return merged_data

def detect_vwap_crossovers(merged_data):
    merged_data['VWAP_Crossover'] = np.where(
        (merged_data['price_close'].shift(1) < merged_data['vwap'].shift(1)) &
        (merged_data['price_close'] > merged_data['vwap']),
        'Bullish',
        np.where(
            (merged_data['price_close'].shift(1) > merged_data['vwap'].shift(1)) &
            (merged_data['price_close'] < merged_data['vwap']),
            'Bearish',
            'None'
        )
    )
    return merged_data

def detect_anomalies(data, benchmark_data):
    merged_data = pd.merge(data, benchmark_data, on='time_period_start', suffixes=('', '_benchmark'))
    merged_data['price_diff'] = merged_data['price_close'] - merged_data['price_close_benchmark']
    
    merged_data = calculate_vwap(merged_data)
    merged_data = detect_price_anomalies(merged_data)
    merged_data = detect_volume_anomalies(merged_data)
    merged_data = detect_vwap_crossovers(merged_data)
    
    return merged_data
