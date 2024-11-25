# Введение в функциональное программирование
# Генераторы.
import time
from turtledemo.penrose import start

print('\nExample 1')

def func_generator(n):
    i = 0
    while i!= n:
        yield i # return
        i += 1

obj = func_generator(10)
print (obj)

for i in obj:
    print (i)

print('\nExample 2')

def fibonacci_v1(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def fibonacci_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_1 = fibonacci_v1(n = 10)
print('fib_1', fib_1)
for value in fib_1:
    print(value)

fib_2 = fibonacci_v2(n = 10)
print('fib_2', fib_2)
for value in fib_2:
    print(value)

print('\nExample 3')

def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for value in fibonacci_v3():
    print(value)
    if value > 100 ** 6:
        break

print('\nExample 4')

start = time.time()

def read_large_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            yield line.strip()

for line in read_large_file("data.txt"):
    print(line)

finish = time.time()

print((finish - start) * 1000)

