#TODO list

import datetime
from datetime import date
from datetime import datetime

from future.backports.datetime import datetime

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы"""

task = str
#deadline = date
today_tasks  = []
tomorrow_tasks  = []
other_tasks  = []
date_2_date = []
current_date = date.today().isoformat()

print(f'Добрый день! Вы находитесь в программе ведения списка дел,\nСегодня {current_date}')
command = input("Введите команду (help - помощь): ")
if command == "help":
    print(HELP)
elif command == "show":
    print(tasks)
elif command == "exit":
    print("Спасибо за использование! До свидания!")
elif command == "add":
    task = input("\nВведите название задачи: ")
    date_ = input("\nВведите (если необходимо) дату выполнения задачи в формате YYYY-MM-DD: ")
    date_2_date = date_.split('-')
    yy = int(date_2_date[0])
    mm = int(date_2_date[1])
    dd = int(date_2_date[2])
    deadline = datetime(yy, mm, dd)
    current_date = datetime.strptime(current_date, "%Y-%m-%d")
    if deadline == current_date:
        today_tasks.append(task)
    elif deadline > current_date:
        tomorrow_tasks.append(task)
    else:
        other_tasks.append(task)
    print("Задача добавлена")
else:
    print("Неизвестная команда")
