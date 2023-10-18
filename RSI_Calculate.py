import requests
import pandas as pd
import finplot as fplt

def get_klines(symbol: str, interval: str, limit: int) -> pd.DataFrame:
    """
    Fetches klines data from Binance API for a given symbol, interval, and limit.

    Args:
        symbol (str): The symbol of the trading pair.
        interval (str): The interval of the klines data (e.g., '1m', '1h').
        limit (int): The number of klines to fetch.

    Returns:
        pd.DataFrame: DataFrame containing the klines data with columns 'time', 'open', 'high', 'low', 'close', and 'volume'.
    """
    klines_url = "https://api.binance.com/api/v3/klines"
    klines_params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    
    response = requests.get(klines_url, params=klines_params)
    response.raise_for_status()
    data = response.json()
    
    columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(data, columns=columns, dtype=float)

    
    df = df.iloc[:, :6]  # Drop unnecessary columns
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    
    rolling_window = 9
    df['conv'] = (df['high'].rolling(window=rolling_window).max() + df['low'].rolling(window=rolling_window).min()) / 2
    rolling_window = 26
    df['base'] = (df['high'].rolling(window=rolling_window).max() + df['low'].rolling(window=rolling_window).min()) / 2
    
    return df

def calculate_RSI(df: pd.DataFrame, n: int = 14) -> pd.Series:
    """
    Calculates the Relative Strength Index (RSI) for a given dataframe.

    Parameters:
    - df: pandas DataFrame - The input dataframe containing the 'close' column.
    - n: int - The window size for calculating the RSI. Default is 14.

    Returns:
    - rsi: pandas Series - The calculated RSI values.
    """
    # Calculate the price difference between consecutive periods
    delta = df['close'].diff()

    # Calculate the gain and loss for each period
    gain = delta.clip(lower=0)
    loss = delta.clip(upper=0).abs()

    # Calculate the average gain and loss over a rolling window
    avg_gain = gain.rolling(window=n, min_periods=1).mean()
    avg_loss = loss.rolling(window=n, min_periods=1).mean()

    # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss

    # Calculate the relative strength index (RSI)
    rsi = 100 - (100 / (1 + rs))

    return rsi

df = get_klines("BTCUSDT", "1h", 1000)
rsi = calculate_RSI(df)

# Plotting the RSI using finplot
fplt.plot(df['time'], rsi, color='#ff9900', legend='RSI')
fplt.show()