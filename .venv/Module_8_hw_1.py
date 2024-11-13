# Домашнее задание по теме "Try и Except"


def add_everything_up_short(a,b):
    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)
    else:
        return round(a + b, 3)

def add_everything_up(a,b):
    try:
        result = a + b
    except TypeError:
        return str(a) + str(b)
    else:
        return round(a + b, 3)



print(add_everything_up_short(123.456, 'строка'))
print(add_everything_up_short('яблоко', 4215))
print(add_everything_up_short(123.456, 7))

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
