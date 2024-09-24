def print_params(a, b, c):
    print(a, b, c)

print_params(1, 2, 3)
print_params("True", True, 3)

def print_params(a=1, b=2, c=3):
    print(a, b, c)

print_params()
print_params(3, 2, 1)
print_params(c='string')
print_params(1, 2, c='string')
print_params(c='string', a=2, b=4)

def print_params(a, *, b, c):
    print(a, b, c)

print_params(33, b=2, c=1)

def print_params(*, a, b, c):
    print(a, b, c)


print_params(a=1, b=2, c=3)
