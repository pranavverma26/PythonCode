# Private(like) attributes and methods :-

# concept Implementations in Python 
# Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # kisi bhi attribute koa private bna na k lya ham  uska aga doa underscore lga deta h.

    def reset_pass(self):
        print(self.__acc_pass)  # now this will not give any error because ya class k andar h.


acc1 = Account("12345","abcde")
print(acc1.acc_no)
#print(acc1.__acc_pass) now if we print this it will give erroe because we make it private..

print(acc1.reset_pass()) # now this will not give any error because ish function koa hmna private nhi kya h.

