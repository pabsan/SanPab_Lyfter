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
    
    def get_transactions(self):
        data = []
        for transaction in self.transactions:
            data.append([
                transaction.transaction_title,
                transaction.amount,
                transaction.category.category_name,
                transaction.transaction_type
            ])
        return data


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
