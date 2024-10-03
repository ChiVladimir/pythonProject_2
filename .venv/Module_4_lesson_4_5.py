# Пространство имен и области видимости.

#import this
import math

#from math import *
#print(globals())

def square(x):
#    global a # замена пространчтва имен
    a = x ** 2 # a находится в локальном пространстве имен, поэтому print(globals()) и print(locals()) показывают свои разные значения
    print(locals())
    return a

def square_2(x):
    d = x * 2
    def even(x):
        d = x * 2
        if d % 2 == 0:
            print('Чётное')
        else:
            print('Нечётное')
    even(x)
    return d


a = 10 # переменная в глобальном пространсте имен
b = square(2)
c = square_2(2)
print (a)
print (b)
print(math.sqrt(a))
print(globals())
# видимость работает только изнутри вовне функции, но не наоборот! Нельзя обратиться из программы к переменной функции
# причем функция внутри функции (even) будет искать переменную сначала внутри себя, потом внутри функции внутри котроой она находится,
# потом внутри программы, а после и внутри внешнего модуля, если мы используем from module_2 import *
# синтаксис - global a, lockal a, nonlockal a