import ccxt
from datetime import datetime   #시간 읽기 편할도록
from pprint import pprint   #프린트 이쁘게
import pandas as pd

'''
#######각 코인의 하루치 시작가격 고점 저점 현재가격 순으로 나옴
binance = ccxt.binance()        # 바낸 API 따옴
ticker = binance.fetch_ticker('LUNA/USDT')      # 루나 티커 가져오기
print(ticker['open'], ticker['high'], ticker['low'], ticker['close'])   #루나 하루 시작가, 고점, 저점, 현재
'''

'''
#######코인의 하루 분봉 나옴. 저거 나누기 부분 다르게 하면 시간 다르게 해서 나오는듯 ?
binance = ccxt.binance()        # 바낸 API 따옴
ohlcvs = binance.fetch_ohlcv('LUNA/USDT')
for x in ohlcvs:
    print(datetime.fromtimestamp(x[0]/1000).strftime('%Y-%m-%d %H:%M:%S'),' ', x[1:])  # 이부분 삭제 금지..! 타임스탬프 쓰는법임.
markets = binance.fetch_tickers()
'''

'''
# 호가창 가져옴   가격/수량
binance = ccxt.binance()        # 바낸 API 따옴
orderbook = binance.fetch_order_book('BTC/USDT')
for ask in orderbook['asks']:
    print(ask[0], ask[1])
'''

# 내 잔고 조회
binance = ccxt.binance({
    'apiKey': '',
    'secret': '',
})

balance = binance.fetch_balance()
pprint(balance['DOGE'])
# 주문 넣기
order_buy = binance.create_limit_buy_order('BTC/USDT', 50, 3.2) # 구매
order_sell = binance.create_limit_sell_order('BTC/USDT', 50, 3.2) # 판매