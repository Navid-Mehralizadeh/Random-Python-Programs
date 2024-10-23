import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import streamlit as st
from datetime import date, timedelta

today = date.today()
d1 = today.strftime("%Y/%m/%d")
end_date = d1

d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y/%m/%d")
start_date = d2

# Ask the user for a company ticker (e.g., AAPL for Apple)
a = input("Enter Any Company Ticker Symbol >>: ")

# Fetch stock data from Yahoo Finance
try:
    data = web.DataReader(name=a, data_source='yahoo', start=start_date, end=end_date)

    # Create a plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(data.index, data["Close"], label="Close Price")
    ax.set_title(f"{a} Stock Prices", fontsize=20)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    plt.legend()
    plt.grid()

    plt.show()

except Exception as e:
    print(f"Error fetching data for {a}. Please check the ticker symbol and try again.")
