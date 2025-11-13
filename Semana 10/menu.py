import os
import actions as a
import time

def clear_screen():
    os.system('cls')

def draw_main_menu():
    menu_options = {
        1:'Enter Students Information',
        2:'Check Students Information',
        3:'Top 3 with Best Avg',
        4:'Check All Avg',
        5:'Export to CSV',
        6:'Import from CSV',
        0:'Exit'
    }
    
    clear_screen()
    print("=== Main Menu ===")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    print("=================")
    return menu_options


def call_enter_information(list_students):
    clear_screen()
    a.enter_students_information(list_students)
    print(f"Processing new students... There are {len(list_students)} students. Please wait!")
    time.sleep(2)


def call_check_information(list_students):
    clear_screen()
    a.check_students_information(list_students)

def start_program(list_students):
    try:
        isOn = True
        while isOn:
            options = draw_main_menu()
            choice = int(input("Enter your choice: "))
            if choice in options:
                if choice == 1:
                    call_enter_information(list_students)
                elif choice == 2:
                    call_check_information(list_students)
                elif choice == 0:
                    print("Goodbye!")
                    isOn = False
    except ValueError as e:
        print(f"Error not an valid option. {e}")

