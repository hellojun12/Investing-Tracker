import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data_storage/portfolio_history.csv")
df_transactions = pd.read_csv("./data_storage/transactions.csv")

df = df.groupby(['date', 'market']).sum()['total_value'].to_frame().reset_index()

df.loc[df['market']=='US', 'total_value'] = df.loc[df['market']=='US', 'total_value'] * 1400

df = df.groupby('date').sum()['total_value'].to_frame().reset_index()


df_cash_in = df_transactions.loc[df_transactions['적요분류']=='cash_in']
df_cash_out = df_transactions.loc[df_transactions['적요분류']=='cash_out']
columns = ['거래일자', '적요명', '정산금액']
print(df_cash_in[columns].groupby('거래일자').sum()['정산금액'])
print(df_cash_out[columns].groupby('거래일자').sum()['정산금액'])
print(df)


