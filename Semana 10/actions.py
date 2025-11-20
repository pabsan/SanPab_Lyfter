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
        return enter_grade(assigment)
    except InvalidGradeError as e:
        print(f"Error on the grade. Error: {e}")
        return enter_grade(assigment)


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
                    if float(student['average_grade']) > float(best_avg) and (i - 1) not in top3_idexes:
                        best_avg = student['average_grade']
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
        print(f"{rank}. Name: {student['name']} | Section: {student['section']} | Average: {student['average_grade']}")
        rank += 1
    print("=========================================")
    input("Press any key to exit")


def calculate_all_avg(students):
    try:
        print("=== Average of averages Students Option ===")
        if len(students) > 0:
            total_avg = 0
            for student in students:
                total_avg += student['average_grade']
            overall_avg = total_avg / len(students)
            print(f"The overall average grade of all students is: {overall_avg:.2f}")
        else:
            print("No students added!")
        print("=========================================")
        input("Press any key to exit")
    except IndexError as e:
        print(f"Found an error in the list of students. Error: {e}")


def is_delete_student_ok(students, name_search, section_search):
    try:
        student_found = False
        i = 0
        for s in students:
            if s.get('name').lower() == name_search.lower() and s.get('section').lower() == section_search.lower():
                answer = input(f"Are you sure you want to delete student {name_search} from section {section_search}? (Y/N) ")
                if answer.lower() in {'y','yes'}:
                    student_found = True
                    students.pop(i)
                break
            i += 1
        return student_found
    except IndexError as e:
        print(f"Found an error in the list of students. Error: {e}")
        return False
    
def delete_student(students):
    print("=== Delete Student Option ===")
    if len(students) > 0:
        name_search = input("Type the student name to delete: ")
        section_search = input("Type the student section to delete (ex: 11B, 7C, 9A, etc): ")
        if is_delete_student_ok(students, name_search, section_search):
            print("Student deleted successfully.")
        else:
            print("Student not found. Cannot delete.")
    else:
        print("No students added!")
    input("Press enter key to exit")