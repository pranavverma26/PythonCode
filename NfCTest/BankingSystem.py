
class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print("Account holder:", self.name)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_no, name, balance, rate):
        super().__init__(account_no, name, balance)
        self.rate = rate

    def show_balance(self):
        super().show_balance()
        print("Interest rate:", self.rate, "%")


class ATM:
    def __init__(self):
        self.accounts = []

    def run(self):
            while True:
                print("\n1. Create Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Show Balance")
                print("5. Exit")
    
                choice = input("Enter choice: ")
    
                if choice == "1":
                    self.create_account()
    
                elif choice in ("2", "3", "4"):
                    account = self.find_account()
    
                    if account is not None:
                        if choice == "2":
                            amount = float(input("Enter amount: "))
                            account.deposit(amount)
    
                        elif choice == "3":
                            amount = float(input("Enter amount: "))
                            account.withdraw(amount)
    
                        else:
                            account.show_balance()
    
                elif choice == "5":
                    print("ATM closed!")
                    break
    
                else:
                    print("Invalid choice!")

    def create_account(self):
        account_no = input("Enter account number: ")
        name = input("Enter name: ")
        balance = float(input("Enter initial balance: "))
        account_type = input("1. Normal  2. Savings: ")

        if account_type == "1":
            account = BankAccount(account_no, name, balance)
        elif account_type == "2":
            rate = float(input("Enter interest rate: "))
            account = SavingsAccount(
                account_no, name, balance, rate
            )
        else:
            print("Invalid account type!")
            return

        self.accounts.append(account)
        print("Account created!")

    def find_account(self):
        account_no = input("Enter account number: ")

        for account in self.accounts:
            if account.account_no == account_no:
                return account

        print("Account not found!")
        return None

    


atm = ATM()
atm.run()
