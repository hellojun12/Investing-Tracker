import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


df_comp = pd.read_csv("./data_storage/spglobal_data/company.csv")
df_price = pd.read_csv('./data_storage/spglobal_data/company_price.csv')

map = df_comp[['tradingitemid', 'ticker_symbol']].set_index('tradingitemid').to_dict()['ticker_symbol']
df_price['tickersymbol'] = df_price['tradingitemid'].map(map)


df_price_adj = df_price.pivot(index='pricingdate', columns='tickersymbol', values='priceclose')
df_price_raw = df_price.pivot(index='pricingdate', columns='tickersymbol', values='priceclose_raw')
####----------

df = pd.read_csv("./data_storage/portfolio_history.csv")

start_date = df['date'].min()
end_date = df['date'].max()

print("="*100)
print(start_date)
print(end_date)

dates = df['date'].unique()


d = df.pivot(index='date', columns='ticker', values='average_price')
c = df[['date', 'ticker', 'average_price']]
print(df_price_raw)


