# Форматирование строк.

#Конкатенация

print("Hello" + ", world!")
print("Hello " + str(1000) + ", world!") # - number only as a string!

# Подстановка

print('My name is %s' %'Bob')
print('My name is %s. I have %s years old. %s' %('Bob', 60, 'qq')) # more than one parameter as a tuple
print('My name is %s. I have %d years old. %s' %('Bob', 60, 'qq'))
print('My name is %s. I have %x years old. %s' %('Bob', 60, 'qq'))
print('My name is %(name)s. I have %(year)s years old.' %{'name':'Bob', 'year':60})

# format

print('I study at the {}-university.'.format('Urban'))
print('I study at the {}{}.'.format('Urban', '-university'))
print('I study at the {0}{1} {0}.'.format('Urban', '-university'))
print('I study at the {title}{postfix} {title}.'.format(title = 'Urban', postfix = '-university'))

# f-строка

print(f'{"Urban" * 2} is the best')




#
# name = 'simple_2.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         print (line, end = '')
#         for char in line:
#             print(char)
#     print(file.tell())
# print(file.read()) # Ошибка, так как завершение with завершает действия с файлом и закрывает его!