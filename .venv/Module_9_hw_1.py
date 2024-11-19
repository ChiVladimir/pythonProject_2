# Домашнее задание по теме
# "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    results = {}
    int_list = list(map(strings_2_numbers, int_list))
    for function in functions:
        key = function.__name__
        value = function(int_list)
        results[key] = value
    return results

def strings_2_numbers(y):
    if isinstance(y, str):
        return int(y)
    else:
        return y


print(apply_all_func([6, '20', 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

