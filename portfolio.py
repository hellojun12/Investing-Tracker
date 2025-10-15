import pandas as pd

class Portfolio:
    """포트폴리오 관리 클래스 - 현금과 주식을 통합 관리"""
    
    def __init__(self):
        self.cash = {"WON": 0.0, "USD": 0.0}
        self.positions = {}  # {ticker: position_info}
        self.portfolio_history = []
        self.transaction_history = []

    def add_cash_transaction(self, transaction_date, currency, amount, transaction_type="입금"):
        """현금 거래 처리 - 정산금액 기반"""
        if currency == "WON":
            self.cash["WON"] += amount
            self.cash["WON"] = round(self.cash["WON"], 0)
        elif currency == "USD":
            self.cash["USD"] += amount
            self.cash["USD"] = round(self.cash["USD"], 2)

        self.transaction_history.append({
            "type": "cash",
            "currency": currency,
            "amount": amount,       
            "transaction_type": transaction_type,
            "date": transaction_date
        })
        
    def add_stock_transaction(self, transaction_date, ticker, name, sec_type, amount, price, market, transaction_category):
        """주식 거래 처리"""
        total_price = amount * price
        market = "US" if market == "USD" else "KR"
        
        if transaction_category == "buy":   
            if ticker in self.positions:
                # 기존 포지션에 추가
                pos = self.positions[ticker]
                pos['amount'] += amount
                pos['total_price'] += total_price
                pos['average_price'] = pos['total_price'] / pos['amount']
            else:
                # 새로운 포지션 생성
                self.positions[ticker] = {
                    'name': name,
                    'type': sec_type,
                    'amount': amount,
                    'market': market,
                    'total_price': total_price,
                    'average_price': price
                }
        
        elif transaction_category == "sell":
            if ticker not in self.positions:
                raise ValueError(f"매도하려는 종목 {ticker}이 포지션에 없습니다.")
            
            pos = self.positions[ticker]
            pos['amount'] -= amount
            pos['total_price'] -= total_price
            
            if pos['amount'] <= 0:
                del self.positions[ticker]
            
            else:
                pos['average_price'] = pos['total_price'] / pos['amount']
        
        elif transaction_category == "stock_split":
            if ticker not in self.positions:
                raise ValueError(f"액면분할/병합하려는 종목 {ticker}이 포지션에 없습니다.")
            
            pos = self.positions[ticker]
            original_amount = pos['amount']
            pos['amount'] = amount
            
            if original_amount > 0:
                pos['average_price'] = pos['total_price'] / pos['amount']

        self.transaction_history.append({
            "type": "stock",
            "ticker": ticker,
            "name": name,
            "amount": amount,
            "price": price,
            "market": market,
            "transaction_type": transaction_category,
            "date": transaction_date
        })
    
    
    def save_portfolio_snapshot(self, date):
        """특정 날짜의 포트폴리오 상태를 저장"""
        snapshot = {
            "date": date,
            "cash": self.cash.copy(),
            "positions": {}
        }
        
        # 포지션 정보를 DataFrame 변환에 적합한 형태로 저장
        for ticker, pos in self.positions.items():
            snapshot["positions"][ticker] = {
                "name": pos["name"],
                "type": pos["type"],
                "market": pos["market"],
                "amount": pos["amount"],
                "average_price": pos["average_price"],
                "total_value": pos["total_price"]
            }
        
        self.portfolio_history.append(snapshot)
    
    def make_portfolio_history(self):
        """포트폴리오 히스토리를 DataFrame으로 변환"""
        rows = []
        
        for snapshot in self.portfolio_history:
            date = snapshot["date"]
            cash = snapshot["cash"]
            positions = snapshot["positions"]
            
            # 현금 행 추가
            rows.append({
                "date": date,
                "ticker": "WON",
                "name": "원화현금",
                "type": "Cash",
                "market": "KR",
                "amount": 1,
                "average_price": cash["WON"],
                "total_value": cash["WON"]
            })
            
            rows.append({
                "date": date,
                "ticker": "USD", 
                "name": "달러현금",
                "type": "Cash",
                "market": "US",
                "amount": 1,
                "average_price": cash["USD"],
                "total_value": cash["USD"]
            })
            
            # 주식 포지션 행 추가
            for ticker, pos in positions.items():
                rows.append({
                    "date": date,
                    "ticker": ticker,
                    "name": pos["name"],
                    "type": pos["type"],
                    "market": pos["market"],
                    "amount": pos["amount"],
                    "average_price": pos["average_price"],
                    "total_value": pos["total_value"]
                })
        
        df = pd.DataFrame(rows)
        df['date'] = pd.to_datetime(df['date'])

        return df