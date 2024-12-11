# Идея Юнит-тестирования

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def add_(a, b):
    return a * 2 + b * 3

def none_(a, b):
    pass


if __name__ == "__main__":
    print(add(100, 10))
    print(sub(100, 10))
    print(mul(100, 10))
    print(div(100, 10))