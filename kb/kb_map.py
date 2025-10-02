REINDEX_COLUMNS = ['거래일자', '거래번호', '적요명', '종목명', '수량/좌수',  '시장구분/\n통화구분', '단가/\n매매기준가', '거래금액', 
    '환율', '정산금액', '외화\n정산금액', '예수금', '외화예수금', '수수료','국외수수료', '소득세', '거래세등','지방소득세','유가잔고수량']

FORMATTED_COLUMNS = ['거래일자', '거래번호', '적요명', '종목명', '수량/좌수',  '시장구분/통화구분', '단가/매매기준가', '거래금액', 
    '환율', '정산금액', '외화정산금액', '예수금', '외화예수금', '수수료','국외수수료', '소득세', '거래세등','지방소득세','유가잔고수량']

TYPE_ERROR_MAP = {
    '유나이티드 에어라인?':'유나이티드 에어라인', 
    '알리바바 그룹 홀딩(A':'알리바바 그룹 홀딩(ADR)', 
    '메타 플랫폼스(페이스':'메타 플랫폼스(페이스북)', 
    'DIREXION DAILY 20Y TREASURY BULL 3X ETF_OLD':'DIREXION 20+Y TREASURY DAILY 3X', 
    '테이크 투 인터랙티브' : '테이크 투 인터렉티브 소프트웨어', 
    '파라마운트 글로벌 B_OLD' : '파라마운트 스카이댄스',
    'DIREXION 20+Y TREASU' : 'DIREXION 20+Y TREASURY DAILY 3X', 
    '레스토랑 브랜즈 인터' : '레스토랑 브랜즈 인터내셔널',
    '글로벌 십 리스' : '글로벌 쉽 리스'
}

STOCK_INFO_MAP = {
    '마이크로소프트': ['MSFT', 'Microsoft Corporation', 'Stock'],
    '보잉': ['BA', 'The Boeing Company', 'Stock'],
    '카니발': ['CCL', 'Carnival Corporation & plc', 'Stock'],
    '애플': ['AAPL', 'Apple Inc.', 'Stock'],
    '아마존닷컴': ['AMZN', 'Amazon.com, Inc.', 'Stock'],
    '모더나': ['MRNA', 'Moderna, Inc.', 'Stock'],
    '화이자': ['PFE', 'Pfizer Inc.', 'Stock'],
    '아메리칸 에어라인스': ['AAL', 'American Airlines Group Inc.', 'Stock'],
    '델타 에어라인스': ['DAL', 'Delta Air Lines, Inc.', 'Stock'],
    '유나이티드 에어라인': ['UAL', 'United Airlines Holdings, Inc.', 'Stock'],
    'AT&T': ['T', 'AT&T Inc.', 'Stock'],
    '알리바바 그룹 홀딩(ADR)': ['BABA', 'Alibaba Group Holding Limited', 'Stock'],
    'TSMC(ADR)': ['TSM', 'Taiwan Semiconductor Manufacturing Company Limited', 'Stock'],
    '치폴레 멕시칸 그릴': ['CMG', 'Chipotle Mexican Grill, Inc.', 'Stock'],
    '액티비전 블리자드': ['ATVI', 'Activision Blizzard, Inc.', 'Stock'],  # 2023년 MSFT 인수로 상장폐지
    '인텔': ['INTC', 'Intel Corporation', 'Stock'],
    '메타 플랫폼스(페이스북)': ['META', 'Meta Platforms, Inc.', 'Stock'],
    '지오 그룹': ['GEO', 'The GEO Group, Inc.', 'Stock'],
    '현대두산인프라코어31': ['현대두산인프라코어31', '현대두산인프라코어31', 'Bond'],
    '삼척블루파워6': ['삼척블루파워6', '삼척블루파워6', 'Bond'],
    'KODEX 미국S&P500선물(H)': ['069500', 'KODEX 미국S&P500선물(H)', 'ETF'],
    'KODEX 미국달러선물인버스': ['261240', 'KODEX 미국달러선물인버스', 'ETF'],
    'DIREXION 20+Y TREASURY DAILY 3X': ['TMF', 'Direxion Daily 20+ Year Treasury Bull 3X Shares', 'ETF'],
    '씨티그룹': ['C', 'Citigroup Inc.', 'Stock'],
    '인모드': ['INMD', 'InMode Ltd.', 'Stock'],
    '뱅크오브아메리카': ['BAC', 'Bank of America Corporation', 'Stock'],
    '알버말': ['ALB', 'Albemarle Corporation', 'Stock'],
    '원메인 홀딩스': ['OMF', 'OneMain Holdings, Inc.', 'Stock'],
    '제너럴 모터스': ['GM', 'General Motors Company', 'Stock'],
    '옥시덴털 페트롤리엄': ['OXY', 'Occidental Petroleum Corporation', 'Stock'],
    '에어비앤비': ['ABNB', 'Airbnb, Inc.', 'Stock'],
    '허츠 글로벌 홀딩스': ['HTZ', 'Hertz Global Holdings, Inc.', 'Stock'],
    '테이크 투 인터렉티브 소프트웨어': ['TTWO', 'Take-Two Interactive Software, Inc.', 'Stock'],
    '파라마운트 스카이댄스': ['PARA', 'Paramount Global', 'Stock'],  # 합병 관련 변동 있음
    '버크셔 해서웨이 B': ['BRK.B', 'Berkshire Hathaway Inc. Class B', 'Stock'],
    '아틀라시언': ['TEAM', 'Atlassian Corporation Plc', 'Stock'],
    '셰브론': ['CVX', 'Chevron Corporation', 'Stock'],
    '레스토랑 브랜즈 인터내셔널': ['QSR', 'Restaurant Brands International Inc.', 'Stock'],
    '크래프트 하인즈': ['KHC', 'The Kraft Heinz Company', 'Stock'],
    '에이비스 버짓 그룹': ['CAR', 'Avis Budget Group, Inc.', 'Stock'],
    'APA': ['APA', 'APA Corporation', 'Stock'],
    '글로벌 쉽 리스': ['GSL', 'Global Ship Lease, Inc.', 'Stock'],
    '페어 아이작': ['FICO', 'Fair Isaac Corporation', 'Stock'],
    '처브': ['CB', 'Chubb Limited', 'Stock'],
    '어도비': ['ADBE', 'Adobe Inc.', 'Stock'],
    '킨로스 골드': ['KGC', 'Kinross Gold Corporation', 'Stock'],
    'T 1.625 11/15/50': ['T 1.625 11/15/50', 'T 1.625 11/15/50', 'Bond'],
}

KB_TO_COMMON_COLUMNS = {
    '거래일자' : 'transaction_date',
    '거래번호' : 'transaction_number',
    '적요명' : 'transaction_type',
    '종목명' : 'ticker',
    '수량/좌수' : 'quantity',
    '시장구분/통화구분' : 'market_type',
    '단가/매매기준가' : 'price',
    '거래금액' : 'amount',
    '환율' : 'exchange_rate',
    '정산금액' : 'settlement_amount',
    '외화정산금액' : 'foreign_settlement_amount',
    '예수금' : 'margin_amount',
    '외화예수금' : 'foreign_margin_amount',
    '수수료' : 'fee',
    '국외수수료' : 'foreign_fee',
    '소득세' : 'tax',
    '거래세등' : 'transaction_tax',
    '지방소득세' : 'local_tax',
    '유가잔고수량' : 'stock_quantity'
}

# 적요명 매핑
# 1. cash_in
# 2. cash_out
# 3. dividend_in
# 4. tax_out
# 5. buy
# 6. sell
# 7. usd_to_won
# 8. won_to_usd
# 9. stock_split
TRANSACTION_TYPE_MAP = {
    '상품간대체입금': 'cash_in',
    '전자금융입금': 'cash_in',
    '대체입금': 'cash_in',
    '전자금융송금 출금': 'cash_out',
    '대체출금': 'cash_out',
    '은행이체 출금': 'cash_out',
    '배당금 입금': 'dividend_in',
    '사채이자 입금': 'dividend_in',
    '사채원금 입금': 'dividend_in',
    '예탁금이용료 입금': 'dividend_in',
    '단수주매각대금 입금': 'dividend_in',
    '해외원천세 출금': 'tax_out',
    '배당세금추징 출금': 'tax_out',
    'ADR FEE 출금': 'tax_out',
    '이자소득세추징 출금': 'tax_out',
    '매수': 'buy',
    '주식장내매수': 'buy',
    '채권장내매수': 'buy',
    '매도': 'sell',
    '주식장내매도': 'sell',
    '채권장내매도': 'sell',
    '채권상환 출고': 'sell',
    '외화매도': 'usd_to_won',
    '원화증거금환전 입금': 'usd_to_won',
    '외화매수': 'won_to_usd',
    '원화증거금환전 출금': 'won_to_usd',
    '글로벌원마켓플러스외화매수 출금': 'won_to_usd',
    '액면분할 입고': 'stock_split',
    '액면병합 입고': 'stock_split'
}