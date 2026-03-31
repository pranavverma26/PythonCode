# Important Topics :-

# There are four pillar of oop :- 1). Abstractio 2). Encapsulation 3). Inheritance 4). Polymorphism

# Abstraction :- Hiding the implementation details of a class and only showing the essential features to the users.

# class k  andar kish tareka sa chja impliment hoa rhi h exactly woa apna hide kr deya(means unnecessary chja hta diya) and user koa sirf important 
# features dkha rha hoa.

# Example :-

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.Start()         # line 19,20 mai joa unnecssary chj hoa h woa print nhi hogi means unnecssary chja hide hoa gyi

# Encapsulation :- Wrapping data and functions into a single unit(object).
# Basically hm ak capsule bna leta h of data and related functions ka, in a single unit and ishi koa hm Encapsulation kh deta h.
# Basically hmna ak class bna de jska andar methods,attributes h or ushi ki hm object bna k use kr rha h.