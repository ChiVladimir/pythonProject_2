# Класс object и метод __new__.
from gevent.subprocess import value


class User:

    ___instance = None

    def __new__(cls, *args, **kwargs):
        print('I am in __new__')
        if cls.___instance is None:
            cls.___instance = super().__new__(cls)

#        return super().__new__(cls)
        return cls.___instance

    def __init__(self, *args, **kwargs):
        print('I am in __init__')
        self.args = args
        self.kwargs = kwargs
        self.name = kwargs.get('name')
#        self.age = kwargs.get('age')
        for key, values in kwargs.items():
            setattr(self, key, values)

print(int.__mro__) # вывод цкпочки наследования
print(User.__mro__)
print(object)


other = [1, 2, 3, 4]
user = {'name':'Den', 'age': 25, 'gender': 'male'}
user_1 = User()
user_2 = User()

print(user_1 is user_2)
print(id(user_1),id(user_2))

user_1 = User(*other,**user)
print(user_1.args)
print(user_1.kwargs)
print(user_1.name)
print(user_1.age)
print(user_1.gender)
