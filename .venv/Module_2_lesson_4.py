while 1 > 0:
    number = int(input("   Enter a number:"))
    if number == 0:
        break  # выходит из цикла по условию
    if number % 2 == 0:
        print("an even number")
        continue  # отправляет цикл в начало по условию
    if number % 2 != 0:
        print("an odd number")
    print(">>>>>>>>>")
print("!end of cicle!")
a = 5
