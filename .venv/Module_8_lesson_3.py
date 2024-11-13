# Сложные моменты и исключения в стеке вызовов функции

#Example 1
def f1(number):
    return 10 / number

def f2():
    print('Have a nice day!_1')
    result_f1 = f1(0)
    return result_f1

try:
    total = f2()
    print(total)
    print('Done')

except ZeroDivisionError as exc:
    print(f'Bот что пошло не так - {exc}, но мы еще на плаву')

else:
    print('Done')
finally:
    print('End of program!("_")')

#Example 2
def f1(number):
    return 10 / number

def f2():
    print('Have a nice day!_2')
    summ = 0
    for i in range(-2, 2):
        summ += f1(i)
        print(summ)
    return summ

try:
    total = f2()
    print('total - ', total)
    print('Done')

except ZeroDivisionError as exc:
    print(f'Bот что пошло не так - {exc}, но мы еще на плаву')

else:
    print('Done')
finally:
    print('End of program!("_")')

#Example 3
def f1(number):
    return 10 / number

def f2():
    print('\nHave a nice day!_3')
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
            print('Done')

        except ZeroDivisionError as exc:
            print(f'Bот что пошло не так - {exc}, но мы еще на плаву')

#    return summ / 1
    return summ / 0

try:
    total = f2()
    print('total - ', total)
    print('Done')

except ZeroDivisionError as exc:
    print(f'Bот что пошло не так - {exc}, но мы b exit')

else:
    print('Done')
finally:
    print('End of program!("_")')

#Example 4
def f1(number):
    return 10 / number

def f2():
    try:
        print('\nHave a nice day!_4')
        result_f1 = f1(0)
        print('result_f1 - ', result_f1)
    except ZeroDivisionError as exc:
            print(f'Bнутри f1 что пошло не так - {exc}, но мы устояли')

    return result_f1 / 0

try:
    f2()
except NameError as exc:
    print(f'Bот что пошло не так - {exc}, но мы b exit')

else:
    print('Done')
finally:
    print('End of program!("_")')