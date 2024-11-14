# Создание исключений

print('\nExample 1 - "raise" errors')

def greet_person(person_name):
    if person_name == "VolanDeMort":
        raise Exception('We not love you!')
    print(f'Hello, {person_name}!')

greet_person('Dear student')
#greet_person('VolanDeMort')

print("\nExample 2")
#
# try:
#     raise NameError("Hello, Bob!")
#
# except NameError as exc:
#     print(f'Exeption type {type(exc)} flying by with parameters{exc.args}')
#     raise
#
print("\nExample 3")

class ProZero(Exception):
    pass

def f(a, b):
    if b == 0:
        raise ProZero('Division by zero is excluded')
    return a / b

print (f(5, 1))
#print (f(5, 0))

print('End of program!("_")')

print("\nExample 4")

class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a, b):
    if b == 0:
        raise ProZero('Division by zero is excluded', {"a":a, "b":b})
    return a / b

try:
    result = f(10,0)
    print(result)
except ProZero as e:
    print ("Today is a not nice day - we caught the error!!")
    print (f'Error message - {e.message}')
    print (f'Additional info - {e.extra_info}')

print('End of program!("_")')
