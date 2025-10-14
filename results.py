import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data_storage/portfolio_history.csv")

condition1 = df['type'].isin(['Stock', 'ETF'])
#condition2 = df['market'].isin(['US'])

securities =df.loc[condition1,'ticker'].unique().tolist()
benchmark = ['SPY']
all_tickers = securities + benchmark

start_date = df['date'].min()
end_date = df['date'].max()

print("="*100)
print(all_tickers)
print(len(all_tickers))
print(start_date)
print(end_date)
print("="*100)

df2 = pd.read_csv("./company.csv")
print(list(df2['tradingitemid']))

df3 = pd.read_csv('./company_price.csv')

print(len(df2['tradingitemid']))
print(len(df3['tradingitemid'].unique()))

a = df2['tradingitemid']
b = df3['tradingitemid'].unique()

for aa in a:
    if aa not in b:
        print (aa)

c = df2.loc[df2['tradingitemid'] == 2586852]
print(c)



# data = yf.download(all_tickers, start=start_date, end=end_date, auto_adjust=False)['Close']
# data = data.ffill().dropna()

# print(data)