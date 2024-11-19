# Введение в функциональное программирование

#Функция - это объект, поэтому можно работать, как с обычными объектами.

def get_russian_names():
    return (["Иван", "Николай", "Мария"])

def get_british_names():
    return (["John", "Nick", "Mary"])

print(get_russian_names())

my_func = get_russian_names
print(type(get_russian_names))
print(get_russian_names.__name__)

print(type(my_func))
print(my_func.__name__)

name_getters = [get_russian_names, get_british_names]

for name_getter in name_getters:
    print(">>>>>", name_getter())

# функции высшего порядка

def adder(args):
    res = 0
    for number in args:
        res += number
    return res

def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res

def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Total - {result}')

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers_as_strings = ["3", "1", 4, "1", 5, "9", "2", "6"]

process_numbers(numbers=my_numbers, function=adder)
process_numbers(numbers=my_numbers, function=multiplier)

# map - применяется к каждому элементу последовательности и формирует новый список результатов

def mul_by_2(x):
    return x * 2

def strings_2_numbers(y):
    if isinstance(y, str):
        return int(y)
    else:
        return y

result = map(mul_by_2, my_numbers)
print(result)
print(list(result))

result = map(strings_2_numbers, numbers_as_strings)
print(list(result))

#filter - вычисляет функцию для каждого элемента и добавляет элемент в список
# результатов только если функция вернёт true

def is_odd(x):
#    print(x % 3)
    return x % 2

result = filter(is_odd, my_numbers)
print(result)
print(list(result))
