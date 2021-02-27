import random
names = ["Aryan", "Astha", "Agamya", "Shobha", "Ajay"]
students_score = {name : random.randint(1,100) for name in names}
passed_students = {student : score for (student,score) in students_score.items() if score >= 40}
print(students_score)
print(passed_students)