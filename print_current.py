import pybithumb as bit
import time
con_key = 
sec_key = 

bithumb = bit.Bithumb(con_key, sec_key)


while True:
    price = bit.get_current_price("XRP")
    print(price)
    detail = bit.get_market_detail("XRP")
    print(detail)
    time.sleep(1)
    
#%%
