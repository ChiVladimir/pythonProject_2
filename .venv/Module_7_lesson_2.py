# Режимы открытия файлов.
from importlib.resources import files
from pprint import pprint

from zope.interface import named

name = 'simple.txt'

file = open(name, 'r') # r - read, w - write, a - append; ab, wb, ab - binary

print(file)

pprint(file.read())
file.close()    #always need to do it


name = 'simple_2.txt'
file = open(name, 'w')
print(file.tell())
file.write('Hello, world!')
file.close()

name = 'simple_2.txt'
file = open(name, 'w')
print(file.seek(30))
file.write('Hello, man!')
file.close()

name = 'simple_2.txt'
file = open(name, 'a')
print(">>>>>>", file.tell())
file.write('\nHello, world!')
file.close()
