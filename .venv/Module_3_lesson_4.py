# Произвольное число параметров

def test_func(*params):
    print(params, type(params))

test_func()
test_func(1,2,3,4,5)


def summator(text, *values, type = "sum"):
    s = 0
    for i in values:
        s += i
    return f'{text}{s}{type}'


print(summator('Count total: ',2,3,4, type = " Summator"))


def info_man(**values):
    print(values, type(values))

info_man(name = "Bob", Course = "Python")

def info_man(**values):
    print(values, type(values))
    for key, value in values.items():
        print(key, value)


info_man(name = "Bob", Course = "Python")


def info_man(*types, name_author = "Rob", **values):
# только в таком порядке - сначала идет параметр или рапаковывается список(в любом прядке), потом словарь, не наоборот. Dict - только последним
    print(values, type(values))
    for key, value in values.items():
        print(key, value)
    print (types, name_author)

info_man(1,2,3,4, name="Bob", Course="Python")

def my_sum(n, *args, txt = "Total sum"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print (txt + ":", s)


my_sum(1, 1,2,3,4,5)
my_sum(2, 2,3,4,5, txt = "Total sum of squares")