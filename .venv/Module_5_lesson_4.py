# Перегрузка операторов


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

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f'{self.name}'

    def __del__(self):
        print(f'{self.name} is over')


den = Human('Den', 22)
max = Human('Max', 22)

print(den < max)
print(den == max)
max.name = 'Den'
print(den == max)
max.birthday()

print(den < max)
print(den == max)
print(den)
print(max)
