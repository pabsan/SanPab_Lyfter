class BankAccount():
    def __init__(self, balance):
        self.balance = balance
    
    def _substract_balance(self, amount):
        self.balance -= amount
    
    
    def _add_balance(self, amount):
        self.balance += amount


class SavingAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    @property
    def min_balance(self):
        return self._min_balance
    
    @min_balance.setter
    def min_balance(self, value):
        if value < 0:
            raise ValueError("You cannot put negative min balance.")
        self._min_balance= value
    
    
    def check_balance(self):
        if self.balance < self.min_balance:
            print(f"Warning! Cannot have less balance than minimal {self.min_balance}. Current balance {self.balance}")
            return False
        else:
            print(f"Your current balance is {self.balance}.\n Minimal balance is {self.min_balance}")
            return True
        
    def withdraw_money(self, amount):
        new_balance = self.balance - amount
        if new_balance < self.min_balance:
            print(f"Cannot have less balance than minimal: {self.min_balance}. Your current balance {self.balance}")
            return False
        else:
            self._substract_balance(amount)
            print(f"Success! You have substracted {amount}. Your new balance is {self.balance}.")
            return True
    

    def deposit_money(self,amount):
        if amount > 0:
            self._add_balance(amount)
            print(f"Success you have deposited {amount} to your account.")
            self.check_balance()
        else:
            print("Cannot add negative or zero")

        

my_account = BankAccount(500)

my_saving_account = SavingAccount(my_account.balance, 600)
print(f"Current balance {my_saving_account.balance}")
my_saving_account.withdraw_money(100) #this should not be allow
print(f"Current balance (after try) {my_saving_account.balance}")

my_saving_account.deposit_money(200)
my_saving_account.deposit_money(0) #test 0
my_saving_account.deposit_money(-100) #test negative
my_saving_account.withdraw_money(100) #Shoul be ok
my_saving_account.withdraw_money(100) #Shoul not be ok

my_saving_account.min_balance = 100 
my_saving_account.withdraw_money(100) #Shoul be ok

#my_saving_account.min_balance = -100 #should fail 
### Found by accident the use of decorators and properties to catch this error.
my_saving_account.check_balance()