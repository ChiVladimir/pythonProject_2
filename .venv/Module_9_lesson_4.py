# Введение в функциональное программирование
# Создание функций на лету
from pprint import pprint
from symtable import Class

print('Example 1 lambda-function')

my_func = lambda x: x + 10

print(my_func(x = 42))
print(type(my_func))
print(my_func.__name__)

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers_2 = [2, 4, 5, 2, 10, 2, 7]

result = map (lambda x: x + 10, my_numbers)
print(list(result))

#Example 2

result = map (lambda x, y: x + y, my_numbers, my_numbers_2)
print(list(result))

# lambda-function has limited usage
# - it is executed by the code execution process (not during compilation) and may reduce performance.
# - you may have problems with large frameworks
# - The lambda function is not designed for complex constructions - if you have more than 3 operators, you need to switch to def
#
print('Example 2')

def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2

    elif n == 3:
        def multiplier(x):
            return x * 3

    else:
        raise Exception("I can do only multiplayer 2 or 3")

    return multiplier

by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)

result = map(by_2, my_numbers)
print(list(result))

result = map(by_3, my_numbers)
print(list(result))

print('Example 3')

def get_multiplier_v2(n):
    def multiplier(x):
        return x * n
    return multiplier

by_5 = get_multiplier_v2(5)
print(by_5(x = 42))

by_10 = get_multiplier_v2(10)
by_100 = get_multiplier_v2(100)

print(list(map(by_10, my_numbers)))
print(list(map(by_100, my_numbers)))

print('Example 4')

def matrix(some_list):

    def multiply_column(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return multiply_column

matrix_on_my_numbers = matrix(my_numbers)

result = map(matrix_on_my_numbers, my_numbers_2)
print(list(result))

my_numbers.extend([10, 20, 30])
result = map(matrix_on_my_numbers, my_numbers_2)
print(list(result))

print('Example 5')

class Multiplayer:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n

by_100500 = Multiplayer(n = 100500)
result = by_100500(x = 42)
print(result)

result = map(by_100500, my_numbers)
print(list(result))