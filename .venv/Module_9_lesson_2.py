# Введение в функциональное программирование
# Списковые, словарные сборки.


def by_3(x):
    return x * 3

def is_odd(x):
    return x % 2

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers_2 = [2, 4, 5, 2, 10, 2, 7]

numbers_as_strings = ["3", "1", 4, "1", 5, "9", "2", "6"]

result = map(by_3, filter(is_odd, my_numbers)) # передавать можно не только переменные или списки,
# но и результаты работы функциии
print(list(result))

# списковые сборки

list_comp_1 = [x * 3 for x in my_numbers] #list comprehensive
print(list_comp_1)

# Условия

list_comp_2 = [x * 3 for x in my_numbers if x % 2] #conditions (no more 1 if!!!!)
print(list_comp_2)

list_comp_3 = [x * 3 if x % 2 else x * 10 for x in my_numbers] # construction with else
print(list_comp_3)

result = [x if type(x) == str else x * 5 for x in numbers_as_strings]
print(result)


list_comp_4 = [x * y for x in my_numbers for y in my_numbers_2] #for two lists
print(list_comp_4)

result = [x * y for x in my_numbers for y in my_numbers_2]
print(result)

result = [x * y for x in my_numbers for y in my_numbers_2 if x % 2]
print(result)

result = [x * y for x in my_numbers for y in my_numbers_2 if x % 2 and  x // 2]
print(result)

# Generation lists and dictionaries

result = {x for x in my_numbers}
print(result)

result = {x: x ** 2 for x in my_numbers}
print(result)