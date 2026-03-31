# Q). Create a class called Order which stores item & its price.
        # use Dunder function __gt__() to convey that:  ,Here __gt__ function refers to greater then.
            # order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price


odr1 = Order("chips",20)
odr2 = Order("tea",15)

print(odr1 > odr2)   # True
print(odr1 < odr2)   # False
    