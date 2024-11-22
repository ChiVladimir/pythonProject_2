# Введение в функциональное программирование
# Итераторы.
import sys
from itertools import repeat

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers_2 = [2, 4, 5, 2, 10, 2, 7]

print('Example 1 - itertools library')

ex_itertator = repeat("4", 100_000)
print(ex_itertator)
print(f"Iterator size = {sys.getsizeof(ex_itertator)}")

ex_str = "4" *100_100
print(f"List size = {sys.getsizeof(ex_str)}")

print('\nExample 2')


class Iter:
    def __init__(self):
        self.first = 'The first element'
        self.second = 'The second element'
        self.third = 'The third element'

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return 'Calculation is finished'
        raise StopIteration()

obj = Iter()
print(obj)

for value in obj:
    print(value)


print('\nExample 3')

def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

for value in fibonacci(n = 10):
    print(value)

print('\nExample 4')

class Fibonacci:

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

fib_iterator = Fibonacci(20)
print(fib_iterator)
for value in fib_iterator:
    print(value)
