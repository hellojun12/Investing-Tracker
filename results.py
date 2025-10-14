import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data_storage/portfolio_history.csv")

condition1 = df['type'].isin(['Stock', 'ETF'])
condition2 = df['market'].isin(['US'])

securities =df.loc[condition1 & condition2, 'ticker'].unique().tolist()
benchmark = ['SPY']
all_tickers = securities + benchmark

start_date = df['date'].min()
end_date = df['date'].max()

print("="*100)
print(all_tickers)
print(start_date)
print(end_date)
print("="*100)

# data = yf.download(all_tickers, start=start_date, end=end_date, auto_adjust=False)['Close']
# data = data.ffill().dropna()

# print(data)