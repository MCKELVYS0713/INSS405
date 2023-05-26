num_users = 3
grades = []

for i in range(num_users):
    grade = float(input("Enter final grade: "))
    grades.append(grade)

mean_grade = sum(grades) / len(grades)

if mean_grade >= 90:
    final_grade = "A"
elif mean_grade >= 80:
    final_grade = "B"
elif mean_grade >= 70:
    final_grade = "C"
elif mean_grade >= 60:
    final_grade = "D"
elif mean_grade >= 50:
    final_grade = "E"
else:
    final_grade = "F"
print("Mean grade:", mean_grade)
print("Final letter grade:", final_grade)