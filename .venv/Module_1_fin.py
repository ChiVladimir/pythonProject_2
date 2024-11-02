# Average grade for students
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = {}
average_grade = set()
students_list_srtd = list (sorted(students))
print("    Average grade for students")

n = 0
while n < len(grades):
    average_grade = sum(grades[n]) / len(grades[n])
    print("\033[1;37;40m Student's Name: \033[0m",students_list_srtd[n],"\t\033[1;37;40m - average grade: \033[0m", round (average_grade, 2))
    n += 1
