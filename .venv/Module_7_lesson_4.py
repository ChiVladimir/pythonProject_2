# Оператор "with"
import io
from pprint import pprint

a = 25
name = 'simple_2.txt'
with open(name, encoding='utf-8') as file:
    for line in file:
        print (line, end = '')
        for char in line:
            print(char)
    print(file.tell())
print(file.read()) # Ошибка, так как завершение with завершает действия с файлом и закрывает его!