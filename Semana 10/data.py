import csv
from pathlib import Path

def export_to_csv(students):
    try:
        if len(students) > 0:
            filename = 'students_data.csv'

            # Column headers
            headers = ["name", "section", "spanish_grade", "english_grade", "socials_grade", "sciense_grade", "average_grade"]

            with open(filename, mode='w',newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(students)
                
            print(f"Students data successfully exported to {filename}")
        else:
            print("No student data to export.")
        input("Press enter key to exit")

    except TypeError as e:
        print(f"Error exporting to JSON: {e}")
        input("Press enter key to exit")


def import_from_csv(filename):
    try:
        data_dict = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_dict.append(row)

        input("Press enter key to exit")
        return data_dict
    except FileNotFoundError as e:
        print(f"Error: File not found. {e}")
        input("Press enter key to exit")
        return []


def check_file_exists():
    try:
        file = Path('students_data.csv')
        if file.exists():
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking file existence: {e}")
        return False
