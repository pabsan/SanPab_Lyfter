from logic import FinanceManagement, Transaction
import json

def get_categories(finance_manager):
    for category in finance_manager.categories:
        print(category.category_name)

def save_data(finance_manager, file_name):
    data = {
        "categories":[],
        "transactions":[]
    }
    for category in finance_manager.categories:
        data["categories"].append({"category_name": category.category_name})
    for transaction in finance_manager.transactions:
        data["transactions"].append({
            "transaction_title": transaction.transaction_title,
            "amount": transaction.amount,
            "category": transaction.category.category_name,
            "transaction_type": transaction.transaction_type,
            "transaction_date": transaction.transaction_date.strftime("%d/%m/%Y")
        })
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        
        #first categories
        finance = FinanceManagement()
        for category in data.get('categories', []):
            finance.add_category(category.get('category_name'))

        #then transactions
        for transaction in data.get('transactions', []):
            finance.add_trasaction_by_data(
                transaction.get('transaction_title'), 
                transaction.get('amount'),
                transaction.get('category'),
                transaction.get('transaction_type'),
                transaction.get('transaction_date'))

        #final output
        return finance

    except FileNotFoundError:
        return FinanceManagement()
    except json.JSONDecodeError:
        return FinanceManagement()

