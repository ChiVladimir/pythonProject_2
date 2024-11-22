# Домашнее задание по теме "Создание функций на лету"
from random import choice

print('Lambda-функция:')

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)

print('Замыкание:')

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'a')
        for i in range(0, len(data_set)):
            row = str(data_set[i]) + '\n'
            file.write(row)
        file.close()

    return write_everything

write = get_advanced_writer('Example_9_4.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print('Метод __call__:')

class MysticBall:

    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


