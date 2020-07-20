import pybithumb as bit
import time
con_key =
sec_key = 

bithumb = bit.Bithumb(con_key, sec_key)
tmp =  int(input("input buy price"))

while True:
    price = bit.get_current_price("XRP")
    print(price)
    detail = bit.get_market_detail("XRP")
    print(detail)
    if type(price) != int:
        time.sleep(1)
        continue
    if(price <= tmp):
        order = bithumb.buy_market_order("XRP", 5)
        print(order)
        print("completed", price)
        break
    time.sleep(1)
    

