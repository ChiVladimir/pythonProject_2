# Домашнее задание по теме "Позиционирование в файле".
# Задача "Записать и запомнить"
import io
from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a')
    for i in range(len(strings)):
        file.write(strings[i])
        file.write('\n')
    file.close()
    file = open(file_name, 'r')
    _len = []
    for i, line in enumerate(file):
        value = line.strip()
        key = (i + 1, sum(_len))
        _len.append(len(line.encode("utf8")) + 1)
        strings_positions[key] = value
    file.close()
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)