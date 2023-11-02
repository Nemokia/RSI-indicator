import pandas as pd
import numpy as np
import requests
import finplot as fplt

def main():
    get_rsi()
def get_rsi(symbol, interval):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
    data = requests.get(url).json()
    df = pd.DataFrame(data)
    df = df.iloc[:,:6]
    df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df.open = df.open.astype(float)
    df.close = df.close.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = abs(avg_gain / avg_loss)
    rsi = 100 - (100 / (1 + rs))
    return rsi

    symbol = 'BTCUSDT'
    interval = '1h'
    rsi = get_rsi(symbol, interval)

    ax,ax2 = fplt.create_plot(symbol, rows=2)

    # plot candle sticks
    candles = pd.DataFrame(requests.get(f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}").json())
    candles = candles.iloc[:,:6]
    candles.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    candles = candles.astype(float)
    fplt.candlestick_ochl(candles[['time','open','close','high','low']], ax=ax)

    # plot RSI
    fplt.plot(rsi, ax=ax2, color='#4a8')

    # plot oversold and overbought levels
    fplt.plot([30]*len(rsi), ax=ax2, color='#4a8', ls='--')
    fplt.plot([70]*len(rsi), ax=ax2, color='#4a8', ls='--')

    # show the plot
    fplt.show()

if __name__ == "__main__":
    main()

