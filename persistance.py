import logic
import json

file_name = "finance_data.json"

def get_categories(finance_manager):
    for category in finance_manager.categories:
        print(category.category_name)

def save_data(finance_manager):
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
            "transaction_type": transaction.transaction_type
        })
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
