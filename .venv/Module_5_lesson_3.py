# Специальные методы классов


class Human:
    def __init__(self, name, age): # dunder - double ander
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print (f'Hello, my name is {self.name}, I have {self.age} years old')

    def birthday(self):
        self.age += 1
        print(f'I have Birthday today, I have {self.age} now')

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'{self.name} is over')


den = Human('Den', 22)
max = Human('Max', 55)
del den
max.birthday()

input()

print (max.__len__())
