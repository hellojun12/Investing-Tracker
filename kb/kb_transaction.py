import numpy as np
import pandas as pd 
from datetime import datetime
from kb_map import REINDEX_COLUMNS, FORMATTED_COLUMNS, TYPE_ERROR_MAP, STOCK_INFO_MAP, TRANSACTION_TYPE_MAP

RAW_DATA_PATH = "./data_storage/trans_raw.xlsx"
RESULT_DATA_PATH = "./data_storage/transactions.csv"

def run():
    df = pd.read_excel(RAW_DATA_PATH, header=None)

    cols = df.iloc[2:5].values
    rows = []
    for i in range(0, len(df)):

        if type(df.iloc[i, 0]) == datetime:
            data = df.iloc[i:i+3].reset_index(drop=True)
            rows.append(data)

    df = pd.concat(rows, axis=0).reset_index(drop=True)

    multi_index = pd.MultiIndex.from_arrays(cols)
    df.columns = multi_index

    df.to_csv(RESULT_DATA_PATH, index=False)
    df = pd.read_csv(RESULT_DATA_PATH, header=None)
    # 2) 3줄씩 묶어서 한 줄로 합치기
    cnt = 0
    columns = []
    rows = []
    for i in range(0, len(df), 3):
        block = df.iloc[i:i+3]
        merged = pd.Series(block.values.flatten())    
        if cnt != 0:
            rows.append(merged)
        else:
            columns.extend(merged)
        cnt+=1

    # 3) DataFrame 만들기
    df = pd.DataFrame(rows)
    df.columns = columns
    df = df.dropna(axis=1, how='all')

    df = df[REINDEX_COLUMNS]
    df.columns = FORMATTED_COLUMNS

    df['종목명'] = df['종목명'].replace(TYPE_ERROR_MAP)
    df[["티커", "영문명", "분류"]] = df["종목명"].map(STOCK_INFO_MAP).apply(pd.Series)

    df['적요분류'] = df['적요명'].map(TRANSACTION_TYPE_MAP)
    return df

if __name__ == '__main__':

    df = run()
    df.to_csv(RESULT_DATA_PATH, index=False)