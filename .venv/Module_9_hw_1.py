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

def strings_2_numbers(int_list):
    if isinstance(int_list, str):
        try:
            result = int(int_list)
            return result
        except ValueError:
            result = len(int_list)
            return result
        else:
            print('Что-то странное!')
    else:
        return int_list


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 'qqqq', 15, 9], len, sum, sorted))

