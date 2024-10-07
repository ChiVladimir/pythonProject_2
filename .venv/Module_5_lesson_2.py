# Классы и объекты
# Атрибуты и методы объекта. Указатель на свой объект в методах
# Атрибуты - переменные внутри класса, методы - функции внутри класса
from urllib3.http2.probe import acquire_and_get


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print (f'Hello, my name is {self.name}, I have {self.age} years old')

    def birthday(self):
        self.age += 1
        print(f'I have Birthday today, I have {self.age} now')


den = Human('Den', 22)
max = Human('Max', 55)

den.surname = 'Popov'
den.age = 23

print(den.name, den.surname, den.age)
print(max.name, max.age)
# print(max.name, max.surname, max.age) - не работает

den.say_info()
max.say_info()
max.birthday()