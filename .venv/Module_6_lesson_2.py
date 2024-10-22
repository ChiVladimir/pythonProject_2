#Доступ к свойствам родителя. Переопределение свойств.


class Human:
    head = True
    _legs = True
    __arms = True   # __ - защищает переменную от переопределения '_Human__arms'

    def say_hello(self):
        print('hello')

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    pass
    # def about(self):
    #     #print('I am a student')
    #     pass
class Teacher(Human):
    pass


human = Human()
human.about()

student = Student()
student.about()

print(dir(human))
print(dir(student))
print(student._Human__arms)