# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        check_num = str
        for i in range(2, res):
            if res % i == 0:
                check_num = "Составное"
                break
            else:
                check_num = "Простое"
        print(check_num)
        return res
    return wrapper

@is_prime
def sum_three(*args):
    return sum(list(args))

result = sum_three(2, 3, 6)
print(result)
