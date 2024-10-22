# Доступ к свойствам родителя. Переопределение свойств.
# Задача "Изменять нельзя получать"


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return f"\033[34;40mМодель: {self.__model}\033[0m"

    def get_horsepower(self):
        return f"\033[34;40mМощность двигателя: {self.__engine_power}\033[0m"

    def get_color(self):
        return f"\033[34;40mЦвет: {self.__color}\033[0m"

    def print_info(self):
        print(Vehicle.get_model(self), Vehicle.get_horsepower(self), Vehicle.get_color(self),
              f"\033[34;40mВладелец: {self.owner}\033[0m", sep='\n')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"\033[38;2;201;100;59mНельзя сменить цвет на {new_color}\033")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()