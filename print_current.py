import pybithumb as bit
import time
import pandas as pd
con_key = 
sec_key = 

bithumb = bit.Bithumb(con_key, sec_key)


cnt = 0
price_list = []

while cnt <= 1000:
    price = bit.get_current_price("XRP")
    print(price)
    detail = bit.get_market_detail("XRP")
    print(detail)
    time.sleep(1)
    cnt += 1
    if type(price) != int:
        continue
    price_list.append(price)
    
    
    
    

df = pd.DataFrame(price_list, columns=["0731"])
df.to_csv('0731.csv', index=False)
#%%
