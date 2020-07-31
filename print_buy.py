import pybithumb as bit
import time
con_key = ""
sec_key = ""

class Queue:
    def __init__(self, max):
        self.max = max
        self.queue = [None]*self.max
        self.size = self.front = 0
        self.rear = None
        
    def is_empty(self):
        return self.size = 0

    def is_full(self):
        if self.rear == None:
            print("queue(is_full) error\n")
            return False
        return self.nex_index(self.rear) == self.front

    def next_index(self, idx):
        return (idx + 1) % self.max

    def enqueue(self):
        if self.is_full():
            raise Exception("queue is full")
        if self.rear == None:
            self.rear = 0
        else:
            self.rear = self.next_index(self.rear)

        self.queue[self.rear] = data
        self.size += 1
        return self.queue[self.rear]


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.queue[self.front] = None
        self.front = self.next_index(self.front)
        return self.queue[self.front]

    def display(self):
        print(self.queue)


price_list = Queue()




def find_center()
    pass
def find_boundary()
    pass
def process()
    pass


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

    

