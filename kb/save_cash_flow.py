import pandas as pd

path = "./data_storage/transactions.csv"
df = pd.read_csv(path)
trans_dates = df['거래일자'].unique()

df_cash_in = df.loc[df['적요분류'] == 'cash_in', ['거래일자', '거래금액']]
df_cash_out = df.loc[df['적요분류'] == 'cash_out', ['거래일자', '거래금액']]
df_cash_out['거래금액'] *= -1

df_in_out = pd.concat([df_cash_in, df_cash_out], axis=0)
df_in_out = df_in_out.sort_index()
df_in_out = df_in_out.set_index('거래일자')
df_in_out.index = pd.to_datetime(df_in_out.index)

df_in_out.index.name = 'transaction_date'
df_in_out = df_in_out.rename(columns={'거래금액':'transaction_amount'})

df_in_out.to_csv('./data_storage/cash_flow.csv')