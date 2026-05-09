import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# STOCK DATA FETCHING
# ==============================

ticker = input("Enter Stock Symbol: ")

df = yf.download(ticker, start="2020-01-01", end="2025-01-01")

# Save CSV backup
df.to_csv(f"{ticker}_stock_data.csv")

print("\nStock Data Preview:\n")
print(df.head())

# ==============================
# DATA CLEANING
# ==============================

df.dropna(inplace=True)

# ==============================
# DAILY RETURNS
# ==============================

df['Daily Return'] = df['Close'].pct_change()

# ==============================
# MOVING AVERAGES
# ==============================

df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# ==============================
# VOLATILITY
# ==============================

volatility = df['Daily Return'].std()

print("\nVolatility:")
print(volatility)

# ==============================
# HIGHEST & LOWEST PRICE
# ==============================

highest_price = df['High'].max()
lowest_price = df['Low'].min()

print("\nHighest Price:", highest_price)
print("Lowest Price:", lowest_price)

# ==============================
# PRICE TREND CHART
# ==============================

plt.figure(figsize=(14,7))

plt.plot(df['Close'], label='Close Price')
plt.plot(df['MA20'], label='20-Day MA')
plt.plot(df['MA50'], label='50-Day MA')

plt.title(f"{ticker} Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.savefig("outputs/price_trend.png")

plt.show()

# ==============================
# DAILY RETURNS DISTRIBUTION
# ==============================

plt.figure(figsize=(10,5))

sns.histplot(df['Daily Return'].dropna(), bins=50)

plt.title("Daily Return Distribution")

plt.savefig("outputs/daily_returns.png")

plt.show()

# ==============================
# FINAL REPORT
# ==============================

report = f"""
Stock Analysis Report
=====================

Ticker: {ticker}

Highest Price: {highest_price}

Lowest Price: {lowest_price}

Volatility: {volatility}

Average Daily Return:
{df['Daily Return'].mean()}
"""

with open("reports/final_report.txt", "w") as f:
    f.write(report)

print("\nReport Generated Successfully!")