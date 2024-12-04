

def is_valid_len(set_1, set_2, length):
        if len(set_1) == len(set_2) == length:
                return True
        else:
                print('Длина последовательностей не совпадает, проверьте, пожалуйста!')
                return False

set_1 = []
set_2 = []
set_1_inp = []
set_2_inp = []
length = int
result =  []

try:
        length = int(input("Введите длину последовательности:"))
        set_1_inp = input("Введите первую последовательность(разделитель - пробел):").split()
        set_2_inp = input("Введите вторую последовательность(разделитель - пробел):").split()
        set_1 = [int(set_1_inp[j]) for j in range(0, len(set_1_inp))]
        set_2 = [int(set_2_inp[j]) for j in range(0, len(set_2_inp))]
except ValueError:
        print('Веден некорректный тип данных, должны вводиться только целые числа')
else:
        if is_valid_len(set_1, set_2, length):
                result = []
                for i in range(0, length):
                        result.append(set_1[i])
                        result.append(set_2[i])
                print(result)
        else:
                exit()