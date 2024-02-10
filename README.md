## README for Bitcoin RSI Plotter

This Python script retrieves historical price data for a cryptocurrency and plots the Relative Strength Index (RSI) indicator alongside the candlestick chart.

### Features:

* Fetches data from the Binance API.
* Calculates RSI based on user-defined symbol and interval.
* Plots candlestick chart using Finplot library.
* Highlights oversold and overbought levels.

### Requirements:

* Python 3.6+
* pandas
* numpy
* requests
* finplot

### Usage:

1. **Install required libraries:**
   ```bash
   pip install pandas numpy requests finplot
   ```
2. **Run the script:**
   ```bash
   python script.py
   ```

**Note:**

* This script is for educational purposes only and should not be used for making investment decisions.
* Adjust the `symbol` and `interval` variables in the `main` function to analyze different cryptocurrencies and timeframes.

### Technical Details:

* The script retrieves data from the Binance API using the `requests` library.
* RSI calculation is based on the following formula:
```
RSI = 100 - (100 / (1 + Avg Gain / Avg Loss))
```
* Finplot library is used to create and customize the chart.
* Oversold and overbought levels are plotted at 30 and 70, respectively.

### Contributing:

Feel free to contribute suggestions, pull requests, and improvements to this project.

### License:

MIT License

### Author:

Nemat Kianezhad
