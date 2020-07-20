import pybithumb as bit
import time
con_key = 
sec_key = 

bithumb = bit.Bithumb(con_key, sec_key)
tmp =  int(input("input sell price"))

while True:
    price = bit.get_current_price("XRP")
    print(price)
    detail = bit.get_market_detail("XRP")
    print(detail)
    if(price >= tmp):
        order = bithumb.sell_market_order("XRP", 5)
        
        print("completed", price)
        break
    time.sleep(1)
    

