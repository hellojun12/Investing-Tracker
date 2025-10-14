import pandas as pd
from portfolio import Portfolio


def process_security_transactions(transaction, date):

    transaction_type = transaction['적요명']
    transaction_category = transaction['적요분류']

    #  거래 처리    
    if transaction_category in ["buy", "sell", "stock_split"]:
        ticker = transaction['티커']
        name = transaction['종목명']
        sec_type = transaction['분류']
        amount = float(transaction['수량/좌수'])
        price = float(transaction['단가/매매기준가'])
        market = transaction['시장구분/통화구분']
        
        portfolio.add_stock_transaction(date, ticker, name, sec_type, amount, price, market, transaction_category)
            

def process_cash_transactions(transaction, date):

    # 현금 거래 처리 - 정산금액 기반
    won_settlement = 0 if pd.isna(transaction['정산금액']) else transaction['정산금액']
    usd_settlement = 0 if pd.isna(transaction['외화정산금액']) else transaction['외화정산금액']
    transaction_type = transaction['적요명']
    currency_ex_rate = transaction['환율']
    transaction_category = transaction['적요분류']

    
    # 원화 정산금액 처리
    if transaction_category in ["cash_in", "dividend_in", "sell", "usd_to_won"]:
        # 입금 거래
        portfolio.add_cash_transaction(date, "WON", float(won_settlement), transaction_type)
    elif transaction_category in ["cash_out", "buy",  "tax_out", "won_to_usd"]:
        # 출금 거래
        portfolio.add_cash_transaction(date, "WON", -float(won_settlement), transaction_type)
    
    elif transaction_category in ['예탁금세액충당매도','세금충당외화매도']:
        # 예탁금 새액충당 매도는 원화표시가 안되어있음
        won_settlement = float(usd_settlement) * float(currency_ex_rate)
        portfolio.add_cash_transaction(date, "WON", float(won_settlement), transaction_type)


    # 달러 정산금액 처리
    if transaction_category in ["cash_in", "dividend_in", "sell", "won_to_usd"]:
        # 달러 입금
        portfolio.add_cash_transaction(date, "USD", float(usd_settlement), transaction_type)
    elif transaction_category in ["cash_out", "buy", "tax_out", "usd_to_won"]:
        # 달러 출금
        portfolio.add_cash_transaction(date, "USD", -float(usd_settlement), transaction_type)

    elif transaction_type in ['예탁금세액충당매도','세금충당외화매도']:
        portfolio.add_cash_transaction(date, "USD", -float(usd_settlement), transaction_type)

    

def run(path, portfolio):

    df = pd.read_csv(path)
    trans_dates = df['거래일자'].unique()
    
    for date in trans_dates:
        daily_transactions = df[df['거래일자'] == date]
        
        for _, transaction in daily_transactions.iterrows():

            process_security_transactions(transaction, date)
            process_cash_transactions(transaction, date)
            
        portfolio.save_portfolio_snapshot(date)

    return portfolio

if __name__ == "__main__":

    path = "./data_storage/transactions.csv"
    portfolio = Portfolio()
    portfolio = run(path, portfolio)
    result = portfolio.make_portfolio_history()
    result.to_csv("./data_storage/portfolio_history.csv", index=False)