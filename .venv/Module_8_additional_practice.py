# Дополнительная практика по модулю 8
# Практика-исключения

def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
#    print(operand_1, operation, operand_1)
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '*':
        value = operand_1 / operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        raise ValueError('Unknown operation {operation}')
    return value

total = 0
with open('data.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
               print(f'Не хватает операндов {exc} в строке {line}')
            else:
                print(f'Не могу преобразовать к целому {exc} в строке {line}')

print(f'Total {total}')
