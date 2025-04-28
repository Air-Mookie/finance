import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def fetch_data(ticker, start_date, end_date):
    """Fetch historical stock data from Yahoo Finance."""
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def preprocess_data(data):
    """Preprocess the stock data."""
    data['Return'] = data['Adj Close'].pct_change()
    data.dropna(inplace=True)
    return data

def visualize_data(data, ticker):
    """Visualize the stock data."""
    plt.figure(figsize=(14, 7))
    plt.plot(data['Adj Close'], label=f'{ticker} Adjusted Close Price')
    plt.title(f'{ticker} Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    ticker = 'AAPL'  # Example ticker
    start_date = '2020-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')
    
    data = fetch_data(ticker, start_date, end_date)
    processed_data = preprocess_data(data)
    visualize_data(processed_data, ticker)

if __name__ == "__main__":
    main()