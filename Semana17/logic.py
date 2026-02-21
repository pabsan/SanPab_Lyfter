from datetime import datetime

class Category:
    def validate_category_name(self, category_name):
        if not isinstance(category_name, str) or category_name.strip() == "":
            return False
        else:
            return True

    def __init__(self,category_name):
        if self.validate_category_name(category_name):
            self.category_name = category_name.strip()
        else:
            self.category_name = None
    
    def __str__(self):
        return self.category_name


class Transaction:
    def validate_transaction_type(self, transaction_type):
        return transaction_type in ['income', 'expense']
    
    def validate_date_format(self, date_str):
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def validate_transaction_title(self, transaction_title):
        if not isinstance(transaction_title, str) or transaction_title.strip() == "":
            return False
        else:
            return True
        
    def validate_category(self, category):
        if not isinstance(category, Category):
            return False
        else:
            return True


    def __init__(self,transaction_title, amount, category, transaction_type, transaction_date=None):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        if not self.validate_transaction_type(transaction_type):
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        if not self.validate_transaction_title(transaction_title):
            raise ValueError("Transaction title must be a non-empty string.")
        if not self.validate_category(category):
            raise ValueError("Category must be an instance of the Category class.")

        
        self.transaction_title = transaction_title.strip()
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        if transaction_date is None:
            transaction_date = datetime.now().strftime("%d/%m/%Y")
        if self.validate_date_format(transaction_date):
            self.transaction_date = datetime.strptime(transaction_date, "%d/%m/%Y")
        else:
            raise ValueError("Date must be in the format dd/mm/yyyy.")      

    def __str__(self):
        return f'Transaction Title: {self.transaction_title} Amount: {self.amount} Category: {self.category.category_name} Type: {self.transaction_type}'



class FinanceManagement:
    def __init__(self):
        self.categories = []
        self.transactions = []

    def validate_category_duplicate(self, category_name):
        for category in self.categories:
            if category.category_name.lower() == category_name.strip().lower():
                return True
        return False
    
    def add_category(self, category_name):
        if not self.validate_category_duplicate(category_name):
            category = Category(category_name)
            if category.category_name is not None:
                self.categories.append(category)
                return "Category added successfully."
            else:
                return "Invalid category name."
        else:
            return "Category already exists."
    

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
    

    def add_trasaction_by_data(self, transaction_title, amount, category_name, transaction_type, transaction_date=None):
        category = None
        for cat in self.categories:
            if cat.category_name.lower() == category_name.strip().lower():
                category = cat
                break
        if category is None:
            raise ValueError("Category not found. Please add the category before adding the transaction.")
        transaction = Transaction(transaction_title, amount, category, transaction_type, transaction_date)
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
    
    def get_transactions(self, start_date=None, end_date=None):
        data = []
        for transaction in self.transactions:
            if start_date is not None and transaction.transaction_date < start_date:
                continue
            if end_date is not None and transaction.transaction_date > end_date:
                continue
            data.append([
                transaction.transaction_title,
                transaction.amount,
                transaction.category.category_name,
                transaction.transaction_type,
                transaction.transaction_date.strftime("%d/%m/%Y")
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
