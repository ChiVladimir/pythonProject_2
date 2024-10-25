#Модуль 6. Дополнительная практика
#Задание "Они все так похожи"

import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = color
        self.filled =bool
        self.__sides = []
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color

    def __is_valid_sides(self, new_sides):
        for i in range(len(new_sides)):
            if self.sides_count != len(new_sides):
                return False
            if new_sides[i] <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        print('init set_sides',self.__sides, self.__color, sides)
        check_sides = True
        for i in range(len(sides)):
            if not isinstance(sides[i], int):
                print('xxxx', sides[i], isinstance(sides[i], int))
                check_sides = False
                break
        if check_sides:
            if len(sides) == 1 and self.sides_count == 12:
                self.__sides = []
                for i in range(self.sides_count):
                    self.__sides.append(*sides)
            elif self.__is_valid_sides(sides):
                self.__sides = [*sides]
            else:
                return self.__sides

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__sides = [*side]
        self.__color = color
        for i in range(0, self.sides_count):
            self.__sides.append(*side)
        self.__sides = list(self.__sides)

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
