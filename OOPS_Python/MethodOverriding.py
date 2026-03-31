# Method Overriding 
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s1=Phone(20000, "Apple", 13)
s=SmartPhone(20000, "Apple", 13)
s1.buy()
print()
s.buy() # as we see both have buy method but here child class buy will execute