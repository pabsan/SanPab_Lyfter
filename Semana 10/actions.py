class InvalidGradeError(Exception):
    def __init__(self):
        super().__init__('Invalid Grade. The grade must be an integer number between 0-100.')

def call_continue_ask():
    flag_continue = True
    while flag_continue == True:
        want_continue = input("Include another student? (Y/N) ")
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
        enter_grade(assigment)
    except InvalidGradeError as e:
        print(f"Error on the grade. Error: {e}")
        enter_grade(assigment)

def add_new_student(name, section, spanish_grade, english_grade, socials_grade, sciense_grade):
    avg = (spanish_grade + english_grade + socials_grade + sciense_grade) / 4
    new_student_dict = {
        "name": name,
        "section": section,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "socials_grade": socials_grade,
        "sciense_grade": sciense_grade,
        "average_grade": avg
    }
    return new_student_dict


def enter_students_information(students):
    print("=== Enter Student Information Option ===")
    want_continue = True
    try:
        while want_continue:
            name = input("Type the student name: ")
            section = input("Type student section (ex: 11B, 7C, 9A, etc): ")
            spanish = enter_grade("Spanish")
            english = enter_grade("English")
            socials = enter_grade("Socials")
            sciense = enter_grade("Science")

            #add data in the dictionary and then into a list of students
            new_student = add_new_student(name, section,spanish, english, socials, sciense)
            students.append(new_student)
            want_continue = call_continue_ask()
            print("==============================")
            
        return students
    except ValueError as e:
        print(f"Invalid grade enter, it must be an integer number. {e}")


def check_students_information(students):
    try:
        if len(students) > 0:
            print("=== Check Student Information Option ===")
            for student in students:
                print(f"-> Name: {student['name']} | Section: {student['section']} | Spanish: {student['spanish_grade']} | English: {student['english_grade']} | Socials: {student['socials_grade']} | Sciense: {student['sciense_grade']} | Average: {student['average_grade']}")
            print("=======================================")
        else:
            print("No students added!")
        input("Press any key to exit")
    except IndexError as e:
        print(f"Found an error in the list of students. Error: {e}")