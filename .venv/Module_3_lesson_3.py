#Распаковка параметров
#    *args(распаковка позиционных параметров), **kwargs (распаковка словарей(проиндексированных списков))



def print_params(a, b, c):
    print(a, b, c)
print_params(1, 2, 3)

def print_params(*params):
    print(params)
    for i in range(0, len(params)):
        print(params[i])

list_ = [1, 2, 3]
print_params(1, 2, 3, 4 ,5, 6, 7)
print_params(1, 2, 3, 4 ,5, 6, 7, (9, 8, 7))
print_params(list_, 2, 3)
print_params(*list_)
print_params(*list_, 4)


dict_ = {'a':1, 'b':2, 'c':3}
print_params(*dict_)

def print_params(**params):
    print(params)

print_params(**dict_)

def print_params(**params):
    for key, value in params.items():
        print(key, value)

print_params(**dict_)

def print_params(a, b, c):
    print(a, b, c)

list_ = (1, 2)
dict_ = {'c':3}
print_params(*list_, **dict_)