import requests
import matplotlib.pyplot as plt

API_KEY = "d8a2p61r01qhv1uvvlogd8a2p61r01qhv1uvvlp0"
symbol = input("Enter stock symbol: ")

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

data = requests.get(url).json()

time_series = data["Time Series (Daily)"]

dates = list(time_series.keys())[:30]
prices = [float(time_series[date]["4. close"]) for date in dates]

dates.reverse()
prices.reverse()

plt.figure(figsize=(12,6))
plt.plot(dates, prices)

plt.title(f"{symbol} Stock Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()