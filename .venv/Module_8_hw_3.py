# Домашнее задание по теме "Создание исключений"

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, _numbers):
        self.model = str(model)
        self.__vin = self.__is_valid_vin(__vin)
        self._numbers = self.__is_valid_numbers(_numbers)


    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 10000000):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return vin_number

    def __is_valid_numbers(self, _numbers):
        if not isinstance(_numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(_numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return _numbers




try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')