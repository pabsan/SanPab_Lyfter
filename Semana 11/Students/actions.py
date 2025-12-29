import re
from student_module import Student_class
from fail_grades_module import FailGrades

class InvalidGradeError(Exception):
    def __init__(self):
        super().__init__('Invalid Grade. The grade must be an integer number between 0-100.')

def is_valid_name(name):
    if len(name) == 0 or bool(re.search(r'\d',name)):
        return False
    return True


def is_valid_section(section):
    if len(section) < 2 or len(section) > 4 or not section[:-1].isdigit() or not section[-1].isalpha():
        return False
    return True


def enter_student_name():
    name = input("Type the student name: ")
    if is_valid_name(name):
        return name
    else:
        print("Invalid name. The name must not be empty or contain numbers.")
        return enter_student_name()


def enter_student_section():
    section = input("Type student section (ex: 11B, 7C, 9A, etc): ")
    if is_valid_section(section):
        return section
    else:
        print("Invalid section. The section must be at least 2 characters, less than 5, start with numbers and have a letter at the end.")
        return enter_student_section()


def student_exists(students, name, section):
    for s in students:
        if s.name.lower() == name.lower() and s.section.lower() == section.lower():
            return True
    return False


def call_confirmation_ask(msg):
    flag_continue = True
    while flag_continue == True:
        want_continue = input(msg)
        if want_continue.lower() in {'n','no'}:
            return False
        elif want_continue.lower() in {'y','yes'}:
            return True
        else:
            print(f"Invalid asnwer please type either: yes, no, y or n. You typed {want_continue}")


def enter_grade(assigment):
    try:
        grade = int(input(f"Type {assigment} grade: "))
        if grade < 0 or grade > 100:
            raise InvalidGradeError()
        return grade
    except ValueError as e:
        print(f"Error on grade, please type an integer. Error: {e}")
        return enter_grade(assigment)
    except InvalidGradeError as e:
        print(f"Error on the grade. Error: {e}")
        return enter_grade(assigment)


def add_new_student(name, section, spanish_grade, english_grade, socials_grade, sciense_grade):
    avg = (spanish_grade + english_grade + socials_grade + sciense_grade) / 4
    student = Student_class(name, section, spanish_grade, english_grade, socials_grade, sciense_grade, avg)
    return student


def enter_students_information(students):
    print("=== Enter Student Information Option ===")
    want_continue = True
    try:
        while want_continue:
            name = enter_student_name()
            section = enter_student_section()
            spanish = enter_grade("Spanish")
            english = enter_grade("English")
            socials = enter_grade("Socials")
            sciense = enter_grade("Science")

            if student_exists(students,name,section):
                print(f"Student {name} in section {section} already exists. Cannot add duplicates.")
            else:
                #add data in the dictionary and then into a list of students
                new_student = add_new_student(name, section,spanish, english, socials, sciense)
                students.append(new_student)
            want_continue = call_confirmation_ask('Do you want to add another student? (Y/N) ')
            print("==============================")
            
        return students
    except ValueError as e:
        print(f"Invalid grade enter, it must be an integer number. {e}")


def check_students_information(students):
    try:
        if len(students) > 0:
            print("=== Check Student Information Option ===")
            for student in students:
                print(f"-> Name: {student.name} | Section: {student.section} | Spanish: {student.spanish} | English: {student.english} | Socials: {student.socials} | Sciense: {student.science} | Average: {student.avg_grade}")
            print("=======================================")
        else:
            print("No students added!")
        input("Press any key to exit")
    except IndexError as e:
        print(f"Found an error in the list of students. Error: {e}")
        

def get_top_3_best_avg(students):
    try:
        top3 = []
        best_student_index = -1
        top3_idexes = []
        count = 1
        # make sure there are at least 3 students
        if len(students) >= 3:
            #get top 3 best averages
            while count <= 3:
                best_avg = -1
                i = 1
                for student in students:
                    if float(student.avg_grade) > float(best_avg) and (i - 1) not in top3_idexes:
                        best_avg = student.avg_grade
                        best_student_index = i - 1
                    i += 1
                top3_idexes.append(best_student_index)
                count += 1
                top3.append(students[best_student_index])
        else:
            print("Not enough students to determine top 3 best averages. Please add more students.")
        return top3
    except IndexError as e:
        print(f"Found an error in the list of students. Error: {e}")
        input("Press any key to exit")
    except TypeError as e:
        print(f"Found an error in the type of data stored. Error: {e}")
        input("Press any key to exit")


def print_top_3_students(students):
    print("=== Top 3 Students with Best Averages ===")
    rank = 1
    top3_students = get_top_3_best_avg(students)
    for student in top3_students:
        print(f"{rank}. Name: {student.name} | Section: {student.section} | Average: {student.avg_grade}")
        rank += 1
    print("=========================================")
    input("Press any key to exit")


def calculate_all_avg(students):
    try:
        print("=== Average of averages Students Option ===")
        if len(students) > 0:
            total_avg = 0.0
            for student in students:
                total_avg += float(student.avg_grade)
            overall_avg = total_avg / len(students)
            print(f"The overall average grade of all students is: {overall_avg:.2f}")
        else:
            print("No students added!")
        print("=========================================")
        input("Press any key to exit")
    except IndexError as e:
        print(f"Found an error in the list of students. Error: {e}")
    except ValueError as e:
        print(f"Found an error in the type of data stored. Error: {e}")


def delete_student_index(students, name_search, section_search):
    try:
        i = 0
        for s in students:
            if s.name.lower() == name_search.lower() and s.section.lower() == section_search.lower():
                return i
            i += 1
        return -1
    except IndexError as e:
        print(f"Found an error in the list of students. Error: {e}")
        return -1
    
def delete_student(students):
    print("=== Delete Student Option ===")
    if len(students) > 0:
        name_search = input("Type the student name to delete: ")
        section_search = input("Type the student section to delete (ex: 11B, 7C, 9A, etc): ")
        index_to_delete = delete_student_index(students, name_search, section_search)
        if index_to_delete != -1:
            ok_delete = call_confirmation_ask(f"Are you sure you want to delete student {name_search} from section {section_search}? (Y/N) ")
            if ok_delete:
                students.pop(index_to_delete)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Student not found. Cannot delete.")
    else:
        print("No students added!")
    input("Press enter key to exit")


def print_failed_grades(students):
    print("=== Students with Failed Grades ===")
    for student in students:
        fails = FailGrades(student)
        if len(fails.fail_grades) > 0:
            print(f"Student Name: {student.name} | Section: {student.section}")
            for fail in fails.fail_grades:
                for key, value in fail.items():
                    print(f"   - {key.capitalize()} Grade: {value}")
    print("==================================")
    input("Press any key to exit")
