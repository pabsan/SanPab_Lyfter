#total exam grades
total_exam_grades = int(input("Please enter total exam grades to enter: "))

count_grades = 1

count_passed = 0
total_passed = 0
count_non_passed = 0
total_non_passed = 0
total_grade = 0

while (count_grades <= total_exam_grades):
    grade = int(input("Please enter grade score: "))
    if grade < 70:
        count_non_passed += 1
        total_non_passed = total_non_passed + grade
    else:
        count_passed += 1
        total_passed = total_passed + grade
    total_grade = total_grade + grade
    count_grades += 1

if (count_non_passed == 0):
    avg_non_passed = 0
else:
    avg_non_passed = total_non_passed / count_non_passed
if (count_passed == 0):
    avg_passed = 0
else:
    avg_passed = total_passed / count_passed
avg_total = total_grade / total_exam_grades

print(f"Total passed {count_passed} with an average of {avg_passed}")
print(f"Total non passed {count_non_passed} with an average of {avg_non_passed}")
print(f"Total general {avg_total}")