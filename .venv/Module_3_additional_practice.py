# Дополнительное практическое задание по модулю 3


def calculate_structure_sum(data):

    for_sum = []
    result = int()
    if isinstance(data, dict):
        data =  list(zip(data.keys(), data.values()))
    for i in range(0, len(data)):

        if isinstance(data[i], int):
            for_sum.append(data[i])

        if isinstance(data[i], str):
            for_sum.append(len(data[i]))

        if isinstance(data[i], tuple):
            for_sum.append(calculate_structure_sum(data[i]))

        if isinstance(data[i], list):
            for_sum.append(calculate_structure_sum(data[i]))

        if isinstance(data[i], dict):
            for_sum.append(calculate_structure_sum(data[i]))

        if isinstance(data[i], set):
            for_sum.append(calculate_structure_sum(tuple(data[i])))

    result = sum(for_sum)

    return result


data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)