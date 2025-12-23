from student_module import Student_class

class FailGrades:
    def __init__(self, student):
        self.student = student


    def get_fail_grades(self):
        """Returns a list of grades that are below 60."""
        fail_grades = []
        
        fail_grades = [grade for grade in self.grades if grade < 60]
        return fail_grades