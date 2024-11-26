# Дополнительная практика по модулю 9

# 1 - написать функцию, которая возвращает функцию повторения двух первых символов n - раз
# 2 - создать массив функций и применить все функции поочередно к аргументу
# 3 - применить все функции поочередно к массиву аргументов


animal = 'bear'
animals = ['rabbit', 'bear', 'fox']

# 1

def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal
    return repeat

test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

# 2

repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)
result = [func(animal) for func in repetitions]
print(result)

# 3

fin_result = [func(x) for func in repetitions for x in animals]
print(fin_result)

fin_result = [func(x) for x in animals for func in repetitions]
print(fin_result)

# one more task
# exclude dubbing of the calculations

def minimize_func(f):
    mem = {}
    def wrapper(*args):
        print(f'args = {args}, mem = {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Function is done, response = {mem[args]}'
        else:
            return f'Function is already done, response = {mem[args]}'
    return wrapper

@minimize_func
def func(a, b):
    print(f'Выполняем функцию({a} и {b})')
    return a ** b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')

