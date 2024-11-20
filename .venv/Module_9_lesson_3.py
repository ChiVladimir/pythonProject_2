# Введение в функциональное программирование
# Генераторные сборки
import time

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers_2 = [2, 4, 5, 2, 10, 2, 7]

numbers_as_strings = ["3", "1", 4, "1", 5, "9", "2", "6"]

start_time = time.time()
print(">>>> Jump one")
result = [x ** 100 for x in my_numbers]
#print(result)
#print(list(result))

for elem in result:
    print (elem)

print(">>once more")

for elem in result: # No answer - generator works oly one time!
    print (elem)

finish_time = time.time()
print(f'Time: {(finish_time-start_time)*1000} milliseconds')


print(">>>> Jump two")

start_time = time.time()
result = (x ** 100 for x in my_numbers)
#print(result)
#print(list(result))

for elem in result:
    print (elem)

finish_time = time.time()
print(f'Time: {(finish_time-start_time)*1000} milliseconds')

ran = range(10, 30)
zp = zip(my_numbers, my_numbers_2)
mp = map(str, my_numbers)

print(ran, zp, mp)
print(list(ran))
print(list(zp))
print(list(mp))