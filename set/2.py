math_students = {"Анна", "Борис", "Виктор", "Дарья", "Елена"}
physics_students = {"Виктор", "Георгий", "Дарья", "Иван", "Ксения", "Анна"}
cs_students = {"Анна", "Виктор", "Елена", "Иван", "Мария"}

# Студентов, которые посещают все три курса
excelent_students = math_students.intersection(physics_students, cs_students)
print(excelent_students)

#Студентов, которые посещают только математику
only_math_students = math_students.difference(physics_students, cs_students)
print(only_math_students)

# Всех уникальных студентов которые посещали только 1 предмет
unic_math = math_students.difference(physics_students, cs_students)
unic_phisics = physics_students.difference(math_students, cs_students)
unic_cs = cs_students.difference(math_students, physics_students)
print(unic_math, unic_phisics, unic_cs)

#Студентов, которые посещают ровно два курса