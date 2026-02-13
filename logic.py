class Category:
    def __init__(self,category_name):
        self.category_name = category_name
    
    def __str__(self):
        return self.category_name


class Transaction:
    def validate_transaction_type(self, transaction_type):
        return transaction_type in ['income', 'expense']

    def __init__(self,transaction_title, amount, category, transaction_type):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if not self.validate_transaction_type(transaction_type):
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        self.transaction_title = transaction_title
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        

    def __str__(self):
        return f'Transaction Title: {self.transaction_title} Amount: {self.amount} Category: {self.category.category_name} Type: {self.transaction_type}'



class FinanceManagement:
    def __init__(self):
        self.categories = []
        self.transactions = []
    
    def add_category(self, category_name):
        category = Category(category_name)
        self.categories.append(category)
    

    def delete_category(self,category):
        found = False
        if len(self.categories) > 0:
            for category_item in self.categories:
                if category_item.category_name == category.category_name:
                    self.categories.remove(category_item)
                    found = True
                    break
        return found
    
    def print_categories(self):
        for category in self.categories:
            print(category)
    

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def add_trasaction_by_data(self, transaction_title, amount, category_name, transaction_type):
        category = None
        for cat in self.categories:
            if cat.category_name ==  category_name:
                category = cat
                break
        if category is None:
            category = Category(category_name)
            self.categories.append(category)
        transaction = Transaction(transaction_title, amount, category, transaction_type)
        self.transactions.append(transaction)
    

    def delete_transaction(self, transaction):
        found = False
        if len(self.transactions) > 0:
            for transaction_item in self.transactions:
                if transaction_item.transaction_title == transaction.transaction_title:
                    self.transactions.remove(transaction_item)
                    found = True
                    break
        return found
    
    def print_transactions(self):
        for transaction in self.transactions:
            print (transaction)


    @property
    def total_income(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == 'income':
                total += transaction.amount
        return total
    
    @property
    def total_expense(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == 'expense':
                total += transaction.amount
        return total
    
    @property
    def balance(self):
        return self.total_income - self.total_expense



if __name__ == "__main__":
    finance_manager = FinanceManagement()
    finance_manager.add_category("Food")
    finance_manager.add_category("Rent")
    finance_manager.add_category("Utilities")

    transaction1 = Transaction("Grocery Shopping", 150, finance_manager.categories[0], "expense")
    transaction2 = Transaction("Monthly Rent", 1000, finance_manager.categories[1], "expense")  
    finance_manager.add_transaction(transaction1)
    finance_manager.add_transaction(transaction2)
    transaction3 = Transaction("Salary", 3000, finance_manager.categories[2], "income")
    #transaction4 = Transaction("Salary", -10, finance_manager.categories[2], "expense") # This will raise a ValueError due to the negative amount
    finance_manager.add_transaction(transaction3)
    print("Categories:")
    finance_manager.print_categories()
    print("\nTransactions:")
    finance_manager.print_transactions()
    print(f"\nTotal Income: {finance_manager.total_income}")
    print(f"Total Expense: {finance_manager.total_expense}")
    print(f"Balance: {finance_manager.balance}")
