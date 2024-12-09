# Интроспекция.
from idlelib.rpc import request_queue
import requests
#help(requests)
#help(requests.get)

some_string = 'I am a string'
some_number = 42
some_list = [some_string, some_number]

def some_function(param, param_2 = 'n/a'):
    print(f'my params is {param} {param_2}')

class SomeClass():
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)

some_object = SomeClass()

print('\nExample 1. Attribute of class __name__\n')

print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)


print('\nExample 2. Type of the objects\n')

print(type(some_number))

print(type(some_number) is int)
print(type(some_number) is list)
print(type(requests))
print(type(requests.get))

print('\nExample 3. "Dir()" function\n')

from pprint import pprint

pprint(dir)
#pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(some_function))
# pprint(dir(SomeClass))
# pprint(dir(some_object))
#pprint(dir(requests))
# pprint(dir(requests.get))

print('\nExample 4.  "Hasattr()" function\n')

attr_name = 'attribute_2'

print(hasattr(some_object, attr_name))      #False
print(hasattr(some_object, 'attribute_1'))  #True
pprint(dir(some_object))

print('\nExample 5.  "Getattr()" function\n')

attr_name = 'attribute_2'

print(getattr(some_object, 'attribute_1'))
print(help(getattr))
print(getattr(some_object, 'attribute_2', "This can't be happening"))

for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))

print('\nExample 6.  "Callable()" function\n')

print(callable(some_string))                        #False
print(callable(some_function))                      #True
print(callable(some_object.attribute_1))            #False
print(callable(some_object.some_class_method))      #True

print('\nExample 7.  "isinstance()" function\n')

print(isinstance(some_number, str))             #False
print(isinstance(some_number, int))             #True
print(isinstance(some_number, SomeClass))       #False
print(isinstance(some_object, SomeClass))       #True

print('\nExample 8.  "inspect()" function\n')

import inspect

print(inspect.ismodule(requests))               #True
print(inspect.isclass(requests))                #False
print(inspect.isfunction(requests))             #False
print(inspect.isbuiltin(requests))              #False

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)