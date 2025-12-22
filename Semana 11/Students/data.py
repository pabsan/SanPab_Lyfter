import csv
from pathlib import Path
import actions as a
from student_module import Student_class

def export_to_csv(students):
    try:
        if len(students) > 0:
            filename = 'students_data.csv'

            with open(filename, mode='w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name", "section", "spanish", "english", "socials", "science", "avg_grade"])
                #writer.writeheader()
                for student in students:
                    writer.writerow([student.name, student.section, student.spanish, student.english, student.socials, student.science, student.avg_grade])              
            print(f"Students data successfully exported to {filename}")
        else:
            print("No student data to export.")
        input("Press enter key to exit")

    except TypeError as e:
        print(f"Error exporting to CSV: {e}")
        input("Press enter key to exit")


def import_from_csv(filename, students):
    try:
        new_list = []
        added = 0
        dups = 0
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row.get('name')
                section = row.get('section')
                if a.student_exists(students, name, section):
                    dups += 1
                    print(f"-- Duplicate student found in CSV: {name} in section {section}. Skipping entry. --")
                else:
                    added += 1
                    new_list.append(Student_class(**row))
        print(f"Import completed. {added} students added, {dups} duplicates skipped.")
        input("Press enter key to exit")
        return new_list
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
