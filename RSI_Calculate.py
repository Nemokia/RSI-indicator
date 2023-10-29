import requests
import pandas as pd
import finplot as fplt
def main():
    calculate_RSI()
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

if __name__ == "__main__":
    main()