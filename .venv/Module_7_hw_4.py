# Домашнее задание по теме "Форматирование строк".


def _tail(tasks_quan):
    tasks_quan_tail = str(tasks_quan)

    if tasks_quan_tail.endswith('1'):
        tail = "а"

    elif tasks_quan_tail.endswith(
            ('0', '5', '6', '7', '8', '9', '0', '5', '6', '7', '8', '9', '11', '12', '13', '14', '15',
             '16', '17', '18', '19')):
        tail = ""
    else:
        tail = "и"
    return tail


#input

team1_num = 5
team2_num = 6
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82

# Использование %

print('В команде %(name)s участников: %(quant_of_parts)s!' %{'name':team1_name, 'quant_of_parts':team1_num})
print('Итого сегодня в командах участников: %s и %s!' %(team1_num, team2_num))

# Использование format()

print('Команда {} решила задач: {}!'.format(team2_name, score_2))
print('{title} решили задачи за {time} с!'.format(title = team2_name, time = (round(team2_time, 2))))

# Использование f-строк

print(f'Команды решили {score_1} и {score_2} задач{_tail(score_2)}.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = team1_name
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = team2_name
else:
    result = 'Ничья!'
print(f'Результат битвы: победа команды {result}!')

tasks_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = time_total / tasks_total

print(f'Сегодня было решено {tasks_total} задач{_tail(tasks_total)}, в среднем по {(round(time_avg, 2))} секунды на задачу!')
