import math
import pandas as pd
def get_sim_df (fn):
 print ('loading... %s' % fn)
 df = pd.read_csv(fn).apply(pd.to_numeric,errors='ignore')
 
 #print df.to_string();print '------'
 
 group = df.groupby(['timestamp'])
 return group
def cal_mid_price (gr_bid_level, gr_ask_level, group_t):
 
 level = 5 
 #gr_rB = gr_bid_level.head(level)
 #gr_rT = gr_ask_level.head(level)
 
 if len(gr_bid_level) > 0 and len(gr_ask_level) > 0:
 bid_top_price = gr_bid_level.iloc[0].price
 bid_top_level_qty = gr_bid_level.iloc[0].quantity
 ask_top_price = gr_ask_level.iloc[0].price
 ask_top_level_qty = gr_ask_level.iloc[0].quantity
 mid_price = (bid_top_price + ask_top_price) * 0.5 #what is mid price?
 mid_type = 'mkt'
 
 mid_price = ((bid_top_price*ask_top_level_qty) + 
(ask_top_price*bid_top_level_qty))/(bid_top_level_qty+ask_top_level_qty)
 mid_price = math.truncate(mid_price, 1)
 
 #print (mid_type, mid_price)
 return (mid_price, bid_top_price, ask_top_price, bid_top_level_qty, 
ask_top_level_qty)
 else:
 print ('Error: serious cal_mid_price')
 return (-1, -1, -2, -1, -1)
raw_data = get_sim_df ('2018-07-22-bithumb-BTC-book.csv')
i =0
while i <= 3600:
 gr_bid_level_e = raw_data.iloc[i].bids
 gr_ask_level_e = raw_data.iloc[i].asks
 
 data = cal_mid_price(gr_bid_level_e,gr_ask_level_e)
 #pandas csv addition 
 df1 = pd.DataFrame(data)
 df1.to_csv(r"C:\Test\data.csv", index = False)