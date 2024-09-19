#print (1)
#print (2)
#print (3)
#
#name = input("Enter your name > ")
#if name == 'Urban': # == - equivalent (не присвоение, а соответствие!)
#    print ('Hello, administrator!')
#print ('Hello, ', name)
#
#
#name = input("Enter your name > ")
#if name == 'Urban':
#    print ('Hello, administrator!')
#if name == 'Bob':
#    print('Hello, master!')
#else:
#    print ('Hello, ', name)

#or/and
number = int(input("   Введите число: ")) #Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0: #Самое тяжелое условие всегда пишем первым!
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print ('Число не подходит')