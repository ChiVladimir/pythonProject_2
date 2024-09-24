def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(3, 2, 1)
print_params(c='string')
print_params(1, 2, c='string')
print_params(c='string', a=2, b=4)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, False, 'test']
values_dict = {'a':True, 'b':2, 'c':'string'}

print_params(*values_list)
print_params(*values_dict)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
