# Рекурсия

def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str_number.replace('0', '')
    first = int(str_number[0])
    if len(str_number) > 1:
        mult = first * get_multiplied_digits(int(str_number[1:]))
        return mult
    return first


result = get_multiplied_digits(402030)
print(result)
