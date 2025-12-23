from student_module import Student_class

class FailGrades:
    def __init__(self, student):
        self.student = student
        self.fail_grades = self.get_fail_grades()

    def get_fail_grades(self):
        """Returns a list of grades that are below 60."""
        fail_grades = []
        if int(self.student.spanish) < 60:
            fail_grades.append({'spanish': self.student.spanish})
        if int(self.student.english) < 60:
            fail_grades.append({'english': self.student.english})
        if int(self.student.socials) < 60:
            fail_grades.append({'socials': self.student.socials})
        if int(self.student.science) < 60:
            fail_grades.append({'science': self.student.science})
        return fail_grades