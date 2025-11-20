import os
import actions as a
import time
import data as d

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
        7:'Delete Student',
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


def call_top_3_best_avg(list_students):
    clear_screen()
    a.print_top_3_students(list_students)


def call_all_avg(list_students):
    clear_screen()
    a.calculate_all_avg(list_students)


def call_export_to_csv(list_students):
    clear_screen()
    d.export_to_csv(list_students)


def call_import_from_csv():
    clear_screen()
    if d.check_file_exists():
        print("File 'students_data.csv' found. Proceeding to import.")
        filename = 'students_data.csv'
        return d.import_from_csv(filename)
    else:
        print("File 'students_data.csv' not found. Cannot import data.")
        input("Press enter key to exit")
        return []


def call_delete_student(list_students):
    clear_screen()
    a.delete_student(list_students)


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
                elif choice == 3:
                    call_top_3_best_avg(list_students)
                elif choice == 4:
                    call_all_avg(list_students)
                elif choice == 5:
                    call_export_to_csv(list_students)
                elif choice == 6:
                    imported_students = call_import_from_csv()
                    if imported_students:
                        list_students.extend(imported_students)
                elif choice == 7:
                    call_delete_student(list_students)
                elif choice == 0:
                    print("Goodbye!")
                    isOn = False
    except ValueError as e:
        print(f"Error not an valid option. {e}")

