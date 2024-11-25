# Введение в функциональное программирование
# Декораторы.
import time
import sys
#from cgitb import reset
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