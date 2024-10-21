# Цели и задачи. Зачем нужно наследование.

class Human:
    head = True

#    def __init__(self):
#        self.about()

    def say_hello(self):
        print('hello')



class Student(Human): # наследуемый или родительский класс
    head = False
    def about(self):
        print('I am a student')

#    def say_hello(self):
#        print('hello')

class Teacher(Human): # наследуемый или родительский класс
    pass
#    def say_hello(self): # - DRY - дублирование
#        print('hello')

#human = Human()
student = Student()
teacher = Teacher()

print (Human.head)
student.about()

#print (student.head) - без ссылки на родительский классвызывает ошибку, тк классы используют свое пространство имен
#print (human.about()) -"-
print (student.head)  # работает, но не наоборот,
student.say_hello()
teacher.say_hello()