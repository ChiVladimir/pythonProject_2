#Модуль 6. Дополнительная практика
#Задание "Они все так похожи"

import math


class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = tuple
        self.__color = tuple
        self.filled =bool

    def get_color(self):
        return self._color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.r = r, self.g = g, self.b = b

    def set_color(self, r, g, b):
        __is_valid_color(r, g, b)

    def is_valid_sides(self, *args):
        self.valid_sides = False
        neg = tuple(i for i in args if i < 0)
        if len(args) == self.__sides:
            self.valid_sides = True
            if len(neg) > 0:
                self.valid_sides = False
        return self.valid_sides

    def get_sides(self):
        return __sides

    def __len__(self, __sides):
        return sum(__sides)

    def set_sides(self, *new_sides):
        print(new_sides)
        self.check_set_sides = True
        for i in range(0, len(new_sides)):
            if not isinstance(new_sides[i], int):
                self.check_set_sides = False
        if is_valid_sides() and self.check_set_sides == True:
            __sides = new_sides

class Cube(Figure):
    sides_count = 12
    def __init__(self, color: tuple, side: int):
        super().__init__()
        self._sides = []
        self.side = side
        self.__color = color
        for i in range(0, 11):
            self._sides.append(side)
        self.__sides = tuple(self._sides)

    def get_volume(self):
        return math.pow(self.side, 3)

#
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
#
