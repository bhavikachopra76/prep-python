def transaction_log(func): #custom decorator
    def wrapper(self, amount):
        print("\nTransaction Started")
        func(self,amount)
        print("Transaction Completed\n")
    return wrapper

class BankAccount: #defining a class

    bank_name = "SecureTrust Bank" #class attributes
    interest_rate = 5.0

    def __init__(self, account_number, holder_name, balance): #defining a constructor
        self.account_number = account_number #instance attributes
        self.holder_name = holder_name
        self.balance = balance
        print(f"Account created successfully for {self.holder_name}")

    @transaction_log #custom decorator
    def deposit(self, amount): #instance method (uses self)
            self.balance += amount
            print(f"Amount of {amount}Rs. Deposited successfully to {self.holder_name}")

    @classmethod
    def interest_rate_change(cls, new_rate): #class method (uses cls)
        if new_rate > 0:
            cls.interest_rate = new_rate
            print(f"Interest rate changed to {cls.interest_rate}")

    @staticmethod
    def is_valid_amount(amount): #static method (no self, no cls, just utility logic related to class)
        return amount > 0

    def get_details(self):
        print("\nBank Name:", BankAccount.bank_name)
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)
        print("Interest Rate:", BankAccount.interest_rate)


acc1 = BankAccount("101", "Bhavika Chopra", 5000)#defining an object
if BankAccount.is_valid_amount(2000):
    acc1.deposit(2000)
BankAccount.interest_rate_change(6.5)#changes for all objects
acc1.get_details()

