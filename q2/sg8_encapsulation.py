class BankAccount: #below all are the properties and methods of the class BankAccount
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = balance 
        
    def set_account_number(self, account_number):
        self.__account_number = account_number
        
    def set_balance(self, NEWbalance): # sets new balance for the account, but checks if the new balance is negative
        if NEWbalance < 0:
            return "Balance must not be a negative number."
        self.__balance = NEWbalance
        
    def get_account_number(self):
        return f"Account Number: {self.__account_number:.2f}"   
    def get_balance(self):
        return f"Balance: {self.__balance:.2f}"
    

a1 = BankAccount(123456, 1000.00) #creating an object of the class BankAccount
print("Account: 1")
print(a1.get_account_number()) #output: 123456
print(a1.get_balance()) #output: 1000.00
print()
print("\nUpdate Balance to -100.00")
print(a1.set_balance(-100.00)) #output: Balance must not be a negative number.
print()
print(a1.get_account_number()) #output: 123456
print(a1.get_balance()) #output: 1000.00
