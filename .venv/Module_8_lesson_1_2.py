# Ошибки

#Syntax error
#test = "aaaaaaaaa
#print(test)

#Exeption

#test = 0
#print(10 / test)

#Try и Except,  else и finally

try:
    i = 0
    print(10 / i)
    print('Done')
except:
    print('Error - division by zero')

try:
    i = 0
    print(10 / i)
    print('Done')
except ZeroDivisionError:
    print('Error - division by zero')

try:
    truba = a + b
    i = 0
    print(truba / i)
    print('Done')
except (ZeroDivisionError, NameError):
    print('Unknown Error - what?')

try:
    truba = a + b
    i = 0
    print(truba / i)
    print('Done')
except ZeroDivisionError:
    print('Error - division by zero')
except NameError:
    print('NameError')

try:
    i = 0
    print(10 / i)
    print('Done')
except ZeroDivisionError as exc:
    print(f'Bот что пошло не так - {exc}, но мы еще на плаву')

try:
    file = open('blabla.txt')
except OSError as exc:
    print(f'Bот что пошло не так - {exc} ({exc.args}), но мы еще на плаву')


# try:
#     ......
#     ......
# except Name_1 as exc_1:
#     print(f'...{exc_1} ({exc_1.args})')
# except Name_2 as exc_2:
#     print(f'...{exc_2} ({exc_2.args})')
# else:
#     print('Done')
# finally:
#     ...... #needed options, for example file.close()

print('Have a nice day!')
i = int(input(' Enter any number:'))
try:
    result = 10 * (1 / i)
except ZeroDivisionError as exc_1:
    print(f'...{exc_1} ({exc_1.args})')
except Name_2 as exc_2:
    print(f'...{exc_2} ({exc_2.args})')
else:
    print('Done')
finally:
    print('End of program!("_")')