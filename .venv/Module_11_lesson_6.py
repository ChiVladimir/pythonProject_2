# Интроспекция.

import sys
from pprint import pprint

#help(sys)

pprint(dir(sys))

print('sys.executable -', sys.executable)
print('sys.platform -', sys.platform)
print('sys.version -', sys.version)
print('sys.version_info -', sys.version_info)
print('sys.argv -', sys.argv)
print('sys.path -', sys.path)
pprint(sys.modules)
#
# print(__builtins__)
# pprint(dir(__builtins__))

# additional functionality

def func(x):
    if sys.version.split(" ")[0] == '3.12.3':
        return x + 10
    else:
        raise Exception('Unacceptable version')

print(func(10))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(10000)
print(factorial(2000))
print(sys.getsizeof(factorial))
