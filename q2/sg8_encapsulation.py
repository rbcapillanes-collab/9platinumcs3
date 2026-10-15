class BankAccount: #below all are the properties and methods of the class BankAccount
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = balance 
        
    def set_account_number(self, account_number): # defines/creates the modifier set_account_number that can change the account number if called and used 
        self.__account_number = account_number
        
    def set_balance(self, NEWbalance): # sets new balance for the account, but checks if the new balance is negative. If negative then it will not accept the new number an will justy give a warning message 
        if NEWbalance < 0:
            return "Balance must not be a negative number."
        self.__balance = NEWbalance
        
    def get_account_number(self): # calls the account number when called 
        return f"Account Number: {self.__account_number:.2f}"   # makes sure the output has two decimal places 
    def get_balance(self): # calls the account number when called 
        return f"Balance: {self.__balance:.2f}" # makes sure the output has two decimal places 
    

a1 = BankAccount(123456, 1000.00) # creating an object of the class BankAccount and has it that so its account_number is "123456" and its balance is "1000.00"
print("Account: 1") # prints "Account: 1" 
print(a1.get_account_number()) # output: 123456
print(a1.get_balance()) # output: 1000.00
print() # prints a blank space so the output looks organized 
print("\nUpdate Balance to -100.00")
print(a1.set_balance(-100.00)) # output: Balance must not be a negative number.
print() # prints a blank space so the output looks organized 
print(a1.get_account_number()) # output: 123456, showed this way because as said earlier the get function calls the account number when called 
print(a1.get_balance()) # output: 1000.00, showed this way because as said earlier the get function calls the account number when called  
