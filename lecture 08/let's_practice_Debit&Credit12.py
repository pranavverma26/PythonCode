# Q 1). Create Account class with 2 attributes - balance & account no.
       #create methods for debit,credit & printing the balance.

class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    # Debit Method :-
    def Debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited" )
        print("Total balance =",self.get_balance())
         

    # Credit Method :-
    def Credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited.")
        print("Total balance =",self.get_balance())
        

    def get_balance(self):
        return self.balance
        


s1 = Account(4590,215689)
s1.Debit(45)
s1.Credit(20)