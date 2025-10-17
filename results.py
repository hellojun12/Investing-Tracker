import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.float_format', '{:.2f}'.format)


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

def expand_portfolio_to_daily(df, end_date=None, freq="D"):
    """
    Expand sparse portfolio snapshots to daily rows by duplicating each snapshot
    until the next snapshot date (exclusive). For the last snapshot, expand up to
    `end_date` (inclusive) if provided.
    """
    out = df.copy()

    # 1) normalize and keep original as snapshot_date
    out['date'] = pd.to_datetime(out['date']).dt.normalize()
    out = out.rename(columns={'date': 'snapshot_date'})

    # 2) compute next snapshot date (exclusive upper bound)
    snaps = pd.Index(sorted(out['snapshot_date'].unique()))
    next_map = {}
    for i, d in enumerate(snaps):
        if i + 1 < len(snaps):
            next_map[d] = snaps[i + 1]  # next snapshot (exclusive)
        else:
            if end_date is not None:
                next_map[d] = pd.to_datetime(end_date).normalize() + pd.Timedelta(days=1)
            else:
                next_map[d] = d + pd.Timedelta(days=1)  # only same day

    out['next_date'] = out['snapshot_date'].map(next_map)

    # 3) build per-row ranges on chosen frequency, inclusive start / exclusive end
    def _make_range(row):
        end_excl = row['next_date'] - pd.Timedelta(days=1)
        rng = pd.date_range(row['snapshot_date'], end_excl, freq=freq)
        # ensure at least one row even if freq skips the day (e.g., B on weekend)
        if len(rng) == 0:
            rng = pd.DatetimeIndex([row['snapshot_date']])
        return rng

    out['date'] = out.apply(_make_range, axis=1)

    # 4) explode to daily rows
    expanded = out.explode('date', ignore_index=True)

    # 5) tidy up — drop helper columns, sort
    expanded.drop(columns=['snapshot_date', 'next_date'], inplace=True)
    if 'ticker' in expanded.columns:
        expanded.sort_values(['date', 'ticker'], inplace=True, ignore_index=True)
    else:
        expanded.sort_values(['date'], inplace=True, ignore_index=True)

    return expanded


df = expand_portfolio_to_daily(df)
df = df[['date', 'ticker', 'type', 'market', 'amount','total_value']]

df_price = df_price.rename(columns={'pricingdate': 'date', 'tickersymbol': 'ticker'})
df_price['date'] = pd.to_datetime(df_price['date'])
#여기서 date를 주말도 늘려야함

new_df = df.merge(df_price[['date','ticker','priceclose_raw']], on=['date', 'ticker'], how='left')

new_df['market_value'] = new_df['priceclose_raw'] * new_df['amount']
new_df.loc[new_df['type'] == 'Cash', 'market_value'] = new_df.loc[new_df['type'] == 'Cash', 'total_value']

print(new_df)

cash_flow = pd.read_csv('./data_storage/cash_flow.csv').set_index('transaction_date')
ex_rate = pd.read_csv('./data_storage/currency.csv')[['Unnamed: 0', 'KRWUSD']].ffill().rename(columns={'Unnamed: 0': 'date'})
ex_rate['date'] = pd.to_datetime(ex_rate['date'])
cash_flow.index.name = 'date'
cash_flow.index = pd.to_datetime(cash_flow.index)


new_df = new_df.merge(ex_rate, on='date', how='left')
new_df['market_value_won'] = new_df['market_value']
new_df.loc[new_df['market'] == 'US', 'market_value_won'] *= new_df.loc[new_df['market'] == 'US', 'KRWUSD'] 

ndf = new_df.groupby('date').sum()['market_value_won']

print(new_df.loc[new_df['date'] == '2025-09-27'])
print(ndf)