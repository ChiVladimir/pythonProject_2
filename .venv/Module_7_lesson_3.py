# Позиционирование в файле.
import io
from pprint import pprint

a = 25
name = 'simple_2.txt'
# file = open(name, 'a')
# print(file.tell()) # - позиция курсора в байтах!!!
# b = file.tell()
# file.seek(a + b)
# print(file.tell())
# file.write('_new text')
# print(file.tell())
#
# file.close()

file = open(name, 'r', encoding='utf-8')

print(file.writable())
print(file.readable())
print(file.seekable())
print(file.buffer)
print(file.closed)
print(file.tell())
pprint(file.read())
print(file.tell())

file.close()
