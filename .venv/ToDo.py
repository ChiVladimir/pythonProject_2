# TODO list

import random

import datetime
from datetime import date
from datetime import datetime

from future.backports.datetime import datetime

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы
random - добавлять случайную задачу на дату Сегодня"""

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]


tasks = {}

# Сегодня, Завтра, 31.12 ...
# [Задача1, Задача2, Задача3]
# Дата -> [Задача1, Задача2, Задача3]

def add_todo(date, task):
  if date in tasks:
      # Дата есть в словаре
      # Добавляем в список задачу
      tasks[date].append(task)
  else:
      # Даты в словаре нет
      # Создаем запись с ключом date
      tasks[date] = []
      tasks[date].append(task)
  print("Задача ", task, " добавлена на дату ", date)



task = str
today_tasks = []
tomorrow_tasks = []
other_tasks = []
date_2_date = []
current_date = date.today().isoformat()

run = True

print(f'Добрый день! Вы находитесь в программе ведения списка дел,\nСегодня {current_date}')

while run == True:
    command = input("Введите команду (help - помощь): ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач в формате YYYY-MM-DD или напишите Сегодня: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет")
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        run = False
        print("Спасибо за использование! До свидания!")
    elif command == "add":
        task = input("\nВведите название задачи: ")
        date = input("\nВведите (если необходимо) дату выполнения задачи в формате YYYY-MM-DD: ")
        add_todo(date, task)

    else:
        print("Неизвестная команда, попробуйте еще раз")
