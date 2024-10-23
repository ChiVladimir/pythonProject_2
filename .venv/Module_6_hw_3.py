#Множественное наследование. Метод Super
#Задача "Мифическое наследование"

class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance = self.x_distance + dx
        return self.x_distance

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance = self.y_distance + dy
        return self.y_distance

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)

    def move(self, dx: int, dy: int):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance
        # res = list()
        # res.append(self.x_distance)
        # res.append(self.y_distance)
        # result = tuple(res)
        # print(result)

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()