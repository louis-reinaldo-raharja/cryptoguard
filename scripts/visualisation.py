import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_prices_and_anomalies(result, base, quote):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                        subplot_titles=(f'{base}/{quote} Price and VWAP', 'Trading Volume'))

    # Price and VWAP plot
    fig.add_trace(go.Scatter(x=result['time_period_start'], y=result['price_close'], name='Price'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=result['time_period_start'], y=result['vwap'], name='VWAP'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=result[result['Price_Anomaly']]['time_period_start'],
                             y=result[result['Price_Anomaly']]['price_close'],
                             mode='markers', name='Price Anomalies',
                             marker=dict(color='red', size=10)),
                  row=1, col=1)

    # Volume plot
    fig.add_trace(go.Bar(x=result['time_period_start'], y=result['volume_traded'], name='Volume'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(x=result[result['Volume_Anomaly']]['time_period_start'],
                             y=result[result['Volume_Anomaly']]['volume_traded'],
                             mode='markers', name='Volume Anomalies',
                             marker=dict(color='orange', size=10)),
                  row=2, col=1)

    fig.update_layout(height=800, width=1200, title_text=f"{base}/{quote} Price, VWAP, and Volume Analysis")
    fig.update_xaxes(title_text="Time", row=2, col=1)
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)

    return fig

def plot_volatility(result, base, quote):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=result['time_period_start'], y=result['volatility'],
                             name='Historical Volatility'))
    fig.add_trace(go.Scatter(x=result[result['volatility_spike']]['time_period_start'],
                             y=result[result['volatility_spike']]['volatility'],
                             mode='markers', name='Volatility Spikes',
                             marker=dict(color='red', size=10)))

    fig.update_layout(title=f'{base}/{quote} Historical Volatility',
                      xaxis_title='Time',
                      yaxis_title='Volatility',
                      height=600, width=1200)

    return fig

def display_price_table(result):
    return result[['time_period_start', 'price_close', 'vwap', 'volume_traded', 'Price_Anomaly', 'Volume_Anomaly', 'volatility', 'volatility_spike']]


def create_large_transactions_chart(large_txs):
    fig = go.Figure(data=[go.Bar(x=large_txs['from'], y=large_txs['value'])])
    fig.update_layout(title="Large Transactions", xaxis_title="From Address", yaxis_title="Transaction Value (ETH)")
    return fig

def create_wallet_transactions_chart(wallet_txs):
    fig = go.Figure(data=[go.Line(x=wallet_txs['timeStamp'], y=wallet_txs['value'])])
    fig.update_layout(title="Wallet Transactions Over Time", xaxis_title="Timestamp", yaxis_title="Transaction Value (ETH)")
    return fig

def create_gauge(value, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkgray"},
            'steps': [
                {'range': [0, 33], 'color': "red"},
                {'range': [33, 66], 'color': "yellow"},
                {'range': [66, 100], 'color': "green"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    return fig