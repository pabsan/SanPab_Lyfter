from logic import FinanceManagement
from persistance import load_data, save_data
import FreeSimpleGUI as sg
from datetime import datetime

def run_gui():
    manager = load_data("finance_data.json")

    layout = [
        [sg.Text("Finance Manager")],
        [sg.Button("Add Category", key="add_category")],
        [sg.Button("Add Expense", key="add_expense")],
        [sg.Button("Add Income", key="add_income")],
        [sg.Button("View Movements", key="view_movements")],
        [sg.Button("Exit")]
    ]

    window = sg.Window("Finance Manager", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "add_category":
            add_category_window(manager)
        elif event == "add_expense":
            add_transaction_window(manager,"expense")
        elif event == "add_income":
            add_transaction_window(manager,"income")
        elif event == "view_movements":
            movements_window(manager)
    window.close()


def add_category_window(manager):
    layout = [
        [sg.Text("Add New Category")],
        [sg.Text("Category Name"), sg.Input(key="category_name")],
        [sg.Listbox(
            values=[cat.category_name for cat in manager.categories],
            size=(30,6),
            key="-CATEGORY-LIST-"
        )],
        [sg.Button("Add Category"), sg.Button("Cancel")]
    ]

    window = sg.Window("Add Category", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == "Add Category":
            category_name = values["category_name"]
            if category_name:
                manager.add_category(category_name)
                save_data(manager,"finance_data.json")
                sg.popup("Category added successfully!")
                window["-CATEGORY-LIST-"].update(
                    [cat.category_name for cat in manager.categories]
                )
            else:
                sg.popup("Please enter a category name.")
    window.close()


def add_transaction_window(manager,transaction_type):
    if not manager.categories:
        sg.popup(f"Please add a category before adding a transaction of type {transaction_type}.")
        return
    
    layout = [
        [sg.Text(f"Add New {transaction_type}")],
        [sg.Text("Title"), sg.Input(key="transaction_title")],
        [sg.Text("Amount"), sg.Input(key="amount")],
        [sg.Text("Category"), sg.Combo(values=[cat.category_name for cat in manager.categories], key="category")],
        [sg.Text("Transaction Date"), sg.Input(key="transaction_date", size=(20,1),readonly=True), sg.CalendarButton("Select Date", target="transaction_date", format="%d/%m/%Y")],
        [sg.Button(f"Add {transaction_type}"), sg.Button("Cancel")]
    ]

    window = sg.Window(f"Add New {transaction_type}",layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == f"Add {transaction_type}":
            title = values["transaction_title"]
            amount = values["amount"]
            category = values["category"]
            t_date = values["transaction_date"]
            try:
                if title and amount and category:
                    manager.add_trasaction_by_data(title,float(amount),category,transaction_type,t_date)
                    save_data(manager,"finance_data.json")
                    sg.popup(f"{transaction_type.capitalize()} added successfully!")
                    break
                else:
                    sg.popup("Please enter valid data!")
            except ValueError:
                sg.popup("Please enter a valid amount.")
    window.close()

def movements_window(manager):
    data = manager.get_transactions()
    layout = [
        [sg.Text("Movements")],
        [sg.Text("Start Date"), sg.Input(key="start_date", size=(20,1),readonly=True), sg.CalendarButton("Select Date", target="start_date", format="%d/%m/%Y")],
        [sg.Text("End Date"), sg.Input(key="end_date", size=(20,1),readonly=True), sg.CalendarButton("Select Date", target="end_date", format="%d/%m/%Y")],
        [sg.Table(
            values = data,
            headings=["Title", "Amount","Category","Type","Date"],
            auto_size_columns=True,
            display_row_numbers=False,
            justification="center",
            num_rows=15,
            key="movements"
        )],
        [sg.Text(f"Total Income: {manager.total_income}")],
        [sg.Text(f"Total Expense: {manager.total_expense}")],
        [sg.Text(f"Balance: {manager.balance}")],
        [sg.Button("Filter"), sg.Button("Reset Filter")],
        [sg.Button("Close")]
    ]

    window = sg.Window("Movements", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Close":
            break
        elif event == "Filter":
            start_date = values["start_date"]
            end_date = values["end_date"]
            try:
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, "%d/%m/%Y")
                    end_date = datetime.strptime(end_date, "%d/%m/%Y")
                    if start_date > end_date:
                        sg.popup("Start date cannot be after end date.")
                        continue
                    filtered_data = manager.get_transactions(start_date,end_date)
                    window["movements"].update(values=filtered_data)
                else:
                    sg.popup("Please select both start and end dates for filtering.")
            except ValueError:
                sg.popup("Please enter valid dates in the format dd/mm/yyyy.")
        elif event == "Reset Filter":
            data = manager.get_transactions()
            window["movements"].update(values=data)


    window.close()




