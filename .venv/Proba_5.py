phone_book = {'Name_1': '+79857624571','Name_2':'+79857624572'}
print (phone_book)
print (phone_book['Name_1'])
phone_book['Name_1'] = '+89857624571'
print (phone_book)
phone_book['Name_3'] = '+99857624571'
print (phone_book)
del phone_book['Name_2']
print (phone_book)
phone_book.update ({'Name_4':'+99857624571',
                    'Name_5':'+99857624571',
                    'Name_6':'+99857624571'})
print (phone_book)
print (phone_book.get('Name_7', 'Такого ключа нет'))
print (phone_book.get('Name_6', 'Такого ключа нет'))

print (phone_book)
phone_book.pop('Name_5')
print (phone_book)
a = phone_book.pop('Name_4')
print(a)
print (phone_book)
# Аналогично функция .pop работает и со списком
list_ = [0, 1, 2, 3, 4 ,5]
print (list_)
b = list_.pop(2)
print(b)
print (list_)

print (phone_book.keys())
print (phone_book.values())
print (phone_book.items())

phone_book_2 = {'Name_10': ['+79857624571', '+79857624579'],'Name_11':'+79857624572', 'Name_12':'+79857624572'}
print (phone_book_2)

# Множества

set_ ={0, 1, 2, 3, 4, 5, 6, 1, 2, 3, True, 'String', (1, 2, 3)}
print(set_)
list_ = [1, 1, 1, 1, 3, 5, 4, 4]
print(set(list_))
list_ = set(list_)
print(list_)
print(list_.discard(1))
print(list_)
print(list_.remove(3))
print(list_)

print (list_.add(7))
print (list_)