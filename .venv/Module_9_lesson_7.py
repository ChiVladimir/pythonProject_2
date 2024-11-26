# Введение в функциональное программирование
# Декораторы.
import time
import sys


import warnings
warnings.simplefilter("ignore", DeprecationWarning)

print('\nExample 1')

def null_decorator(func):
    return func

def greet():
    return "Hello!"

greet = null_decorator(greet)

print(greet())

print('\nExample 2')

def null_decorator(func):
    return func

@null_decorator
def greet():
    return "Hello!"

print(greet())

print('\nExample 3')

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'
print(greet())

print('\nExample 4')

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def greet():
    return 'Hello!'

greet_dec = uppercase(greet)

print(greet())
print(greet_dec())

print('\nExample 5')

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f"Function's work time is {elapsed} sec")
        return result
    return surrogate

@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
warnings.simplefilter("ignore", DeprecationWarning)
print(result)

print('\nExample 6')

def func_gen_dec(precision):
    print("получили точность")
    print("начинаем создавать декоратор")
    def dec(func):
        print(f"декоратор принял на вход функцию {func}")
        print("начинаем создавать функцию-обертку")
        def wrapper(*args, **kwargs):
            print("мы попали в функцию-обертку, она заместит функцию func")
            print("засекаем время")
            started_at = time.time()
            print("Запускаем реальную функцию с переданными параметрами")
            result = func(*args, **kwargs)
            print("останавливаем секундомер")
            ended_at = time.time()
            print(f"заполняется хронометраж с количеством знаков после запятой - {precision}")
            elapsed = round(ended_at - started_at, precision)
            print(f"Function's work time is {elapsed} sec")
            print("возвращаем результат первоначальной функции")
            return result
        print("возвращаем обертку")
        return wrapper
    print("возвращаем декоратор")
    return dec

def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10**5)

time_track_precision_6 = func_gen_dec(precision=3) #@func_get_dec(precision=2)
digits = time_track_precision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)

