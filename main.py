import ccxt
import pandas as pandas
import pandas as pd
from datetime import datetime   #시간 읽기 편할도록
from pprint import pprint   #프린트 이쁘게
import time



'''
#######각 코인의 하루치 시작가격 고점 저점 현재가격 순으로 나옴
binance = ccxt.binance()        # 바낸 API 따옴
ticker = binance.fetch_ticker('LUNA/USDT')      # 루나 티커 가져오기
print(ticker['open'], ticker['high'], ticker['low'], ticker['close'])   #루나 하루 시작가, 고점, 저점, 현재



#######코인의 하루 분봉 나옴. 저거 나누기 부분 다르게 하면 시간 다르게 해서 나오는듯 ?
binance = ccxt.binance()        # 바낸 API 따옴
ohlcvs = binance.fetch_ohlcv('LUNA/USDT')
for x in ohlcvs:
    print(datetime.fromtimestamp(x[0]/1000).strftime('%Y-%m-%d %H:%M:%S'),' ', x[1:])  # 이부분 삭제 금지..! 타임스탬프 쓰는법임.
markets = binance.fetch_tickers()



# 호가창 가져옴   가격/수량
binance = ccxt.binance()        # 바낸 API 따옴
orderbook = binance.fetch_order_book('BTC/USDT')
for ask in orderbook['asks']:
    print(ask[0], ask[1])


# 내 잔고 조회
binance = ccxt.binance({
    'apiKey': 'u2xlruAHm6iz2EFmW5dOcHRvymKnhMtvfJGbd5snj4rOwr8Qtt3GweEtsPztttW2',
    'secret': 'GjGhPyWVx60PKp5HlfGyfPCfkltn1RrTQbIlkKDCLjzMLKtoAE6eeafz7RUqoQUn',
})

balance = binance.fetch_balance()
pprint(balance['DOGE'])
# 주문 넣기
order_buy = binance.create_limit_buy_order('BTC/USDT', 50, 3.2) # 구매
order_sell = binance.create_limit_sell_order('BTC/USDT', 50, 3.2) # 판매
'''

with open('api.txt') as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options':{
        'defaultType': 'future'
    }
})

'''
markets = binance.load_markets()
for m in markets:
    print(m)
'''
#balance = binance.fetch_balance(params={"type": "future"})
#pprint(balance)

#btc = binance.fetch_ticker("LUNA/USDT") #현재가 조회

#루나코인 15일치 데이터
'''
luna = binance.fetch_ohlcv(
    symbol = "LUNA/USDT",
    timeframe = '1d',
    since=None,
    limit=15)


df = pd.DataFrame(btc, columns=['datetime','open','high','low','close','volume'])
df['datetime'] = pd.to_datetime(df['datetime'],unit='ms')
df.set_index('datetime',inplace=True)
print(df)
'''

'''
########레버리지 조절하고 롱#######
markets = binance.load_markets()
symbol = "LUNA/USDT"
market = binance.market(symbol)
leverage =5

resp = binance.fapiPrivate_post_leverage({
    'symbol': market['id'],
    'leverage': leverage
})

order = binance.create_market_buy_order(
    symbol = symbol,
    amount = 1
)
'''

'''
# 미체결 주문 보여주는거
# 시간으로 해서 3분 넘어가는 미체결 건은 바로 없애기.
balance = binance.fetch_balance()
positions = balance['info']['positions']

for position in positions:
    if position['symbol'] == "LUNAUSDT":
        pprint(position)

open_orders = binance.fetch_open_orders(
    symbol="LUNA/USDT"
)
pprint(open_orders)
'''

'''
# 초당 한번씩 비트코인 가격이랑 시간 나오게하기
symbol = "BTC/USDT"
while True:
    btc = binance.fetch_ticker(symbol)
    now = datetime.now()
    print(now.strftime('%H:%M:%S'),btc['last'])
    time.sleep(1)
'''

symbol = "BTC/USDT"
btc = binance.fetch_ohlcv(
    symbol = symbol,
    timeframe = '1d',
    since=None,
    limit=10
)

df = pd.DataFrame(
    data = btc,
    columns=['datetime','open','high','low','close','volume']
)
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime',inplace=True)

yesterday = df.iloc[-2]
today = df.iloc[-1]
target = today['open'] + (yesterday['high'] - yesterday['low']) * 0.5
print(target)
print(df)




























