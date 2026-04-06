import pytest
from logic import FinanceManagement

@pytest.fixture
def manager():
    my_manager = FinanceManagement()
    my_manager.add_category("Food")
    my_manager.add_category("Transport")
    return my_manager

def test_adding_category(manager):
    #Arrange & Act
    manager.add_category("Rent")
    #Assert
    assert len(manager.categories) == 3 and manager.categories[2].category_name == "Rent"


def test_adding_transaction_by_data(manager):
    #Arrange & Act
    manager.add_trasaction_by_data("Grocery Shopping", 50, "Food", "expense")
    #Assert
    assert len(manager.transactions) == 1 and manager.transactions[0].transaction_title == "Grocery Shopping" and manager.transactions[0].amount == 50 and manager.transactions[0].category.category_name == "Food" and manager.transactions[0].transaction_type == "expense"


def test_try_negative_amount_transaction(manager):
    #Arrange
    amount = -100
    #Act and Assert
    with pytest.raises(ValueError):
        manager.add_trasaction_by_data("My Fault",amount,"Transport","expense")


def test_try_add_invalid_transaction_type(manager):
    #Arrange
    t_type = "Hello"
    #Act and Assert
    with pytest.raises(ValueError):
        manager.add_trasaction_by_data("My Fault",10,"Transport",t_type)


def test_total_income(manager):
    #Arrange and act
    manager.add_trasaction_by_data("Job",1000,"Salary","income")
    manager.add_trasaction_by_data("Extras",100,"Salary","income")
    #Assert
    assert manager.total_income == 1100

def test_total_expense(manager):
    #Arrange and act
    manager.add_trasaction_by_data("Lunch",25,"Food","expense")
    #Assert
    assert manager.total_expense == 25


def test_total_balance_with_income_and_expense(manager):
    #Arrange and act
    manager.add_trasaction_by_data("Job", 1000, "Salary", "income")
    manager.add_trasaction_by_data("Lunch", 200, "Food", "expense")
    #assert
    assert manager.balance == 800


def test_try_add_transaction_with_non_numeric_amount(manager):
    #Arrange
    amount = "Not a number"
    #Act and Assert
    with pytest.raises(ValueError):
        manager.add_trasaction_by_data("My Fault",amount,"Transport","expense")