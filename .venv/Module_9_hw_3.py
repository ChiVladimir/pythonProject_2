# Домашнее задание по теме "Генераторные сборки"


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = list(len(list(zip(first, second))[i][0]) - len(list(zip(first, second))[i][1])
                    for i in range(0, len(list(zip(first, second))))
                    if len(list(zip(first, second))[i][0]) - len(list(zip(first, second))[i][1]) != 0)
print(first_result)
second_result = list(len((first + second)[i]) == len((first + second)[i + int(len(first + second) / 2)])
                     for i in range(0, int(len(first + second) / 2)))
print(second_result)
