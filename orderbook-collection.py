import pybithumb as bi
import time 
import datetime
f = open ('오더북.txt', 'w')
f.write('price /quantity/type/timestamp\n')
f.close()
while True:
 f = open('오더북.txt', 'a')
 
 orderbook = bi.get_orderbook("BTC")
 bids = orderbook['bids']
 asks = orderbook['asks']
 now= str(orderbook['timestamp'])
 timestamp = now[ : 10]
 _date = 
datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%
S')
 for i in bids:
 price = str(i['price'])
 quantity = str(i['quantity'])
 f.write(price)
 f.write('/')
 f.write(quantity)
 f.write('/')
 f.write('0')
 f.write('/')
 f.write(_date)
 f.write('\n')
 
 for j in asks:
 price = str(j['price'])
 quantity = str(j['quantity'])
 f.write(price)
 f.write('/')
 f.write(quantity)
 f.write('/')
 f.write('1')
 f.write('/')
 f.write(_date)
 f.write('\n')
 
 f.close()
 print('good')
 time.sleep(1)