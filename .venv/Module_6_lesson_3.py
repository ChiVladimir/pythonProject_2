#Множественное наследование. Метод Super


class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Hello, my name is {self.name}')

class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} is learning in the Group {self.group}')

class Student(Human, StudentGroup): # Иерархия множественного наследования
    def __init__(self, name, place, group):
#        Human.__init__(self, name) - Допустимый синтаксис, но некорректный
        super().__init__(name, group)
        self.place = place
        super().info()




# human = Human("Bob")
# print(human.name)
#
student = Student('Rob', 'Piter', 'Piton_1')
# print(student.name, student.place)
print(Student.mro()) # оператор дает понимание в последовательности иерархии множественного наследования.
