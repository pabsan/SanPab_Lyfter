from logic import FinanceManagement, Transaction
from persistance import save_data


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
    save_data(finance_manager)
    #print("Categories:")
    #finance_manager.print_categories()
    #print("\nTransactions:")
    #finance_manager.print_transactions()
    #print(f"\nTotal Income: {finance_manager.total_income}")
    #print(f"Total Expense: {finance_manager.total_expense}")
    #print(f"Balance: {finance_manager.balance}")
