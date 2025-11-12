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


def enter_students_information():
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
            want_continue = call_continue_ask()
            print("==============================")
            
        return name
    except ValueError as e:
        print(f"Invalid grade enter, it must be an integer number. {e}")
