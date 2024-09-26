# Встроенные функции в Python

# int()  --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary)/len(salary), 2), ' - средняя зарплата в компании')
print(round(max(salary), 2), ' - максимальная зарплата в компании')
print(round(min(salary), 2), ' - минимальная зарплата в компании')

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = dict(zip(names, salary))
print(zipped['Денис'], '- зарплата Дениса')

a = [1, 1, 1]
b = ''
d = [1, 1, 1]
c = d
c[0] = 2
print(c)
print(d)
print(id(a))
print(id(d))
print(id(c))
print(c is d)


def helper():
    """
    Эта функция-помощник
    """
    pass

print(helper.__doc__)

a = [True, False, False]
print(a)
print ('any', any(a))
print ('all', all(a))
print('---------------------')
a = [False, False, False]
print(a)
print ('any', any(a))
print ('all', all(a))
print('---------------------')
a = [True, True, True]
print(a)
print ('any', any(a))
print ('all', all(a))
print('---------------------')
a = [1, 0, 0]
print(a)
print ('any', any(a))
print ('all', all(a))
print('---------------------')
a = [0, 0, 0]
print(a)
print ('any', any(a))
print ('all', all(a))
print('---------------------')
a = [1, 1, 0]
print(a)
print ('any', any(a))
print ('all', all(a))
print('---------------------')
b = '0'
print(b)
print (any(b))
print('---------------------')
b = ''
print(b)
print (any(b))
print('---------------------')

# Интроспекция - доступные методы

print (dir(a))
print('---------------------')
print (dir(b))
print('---------------------')
print(type(a), type(b))
print('---------------------')
print(isinstance(a, str), isinstance(b, str))
print(isinstance(a, int), isinstance(b, int))
print(type(b) == str)

print('---------------------')
a = [1, 1, 1]
d = [1, 1, 1]
c = d
print(id(a))
print(id(d))
print(id(c))
print(a is d)
print(c is d)
print(id(1))
print(id(1))
print(id(256))
print(id(256))
print(id(9999256))
print(id(9999256))
print('---------------------')
#print(help())
print('---------------------')
print(help(print))
print('---------------------')
print(help(id))
print('---------------------')