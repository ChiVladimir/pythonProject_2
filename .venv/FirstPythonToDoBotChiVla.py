import telebot
from random import choice
from datetime import datetime
from telebot import types

token = "7508012660:AAF4rN0oF69gMfDOEBNl6EhHPu-hq9a29ME"
bot = telebot.TeleBot(token)
RANDOM_TASKS = ['Написать письмо', 'Выучить Python', 'Записаться на курс кройки и шитья', 'Посмотреть 4 сезон Рик и Морти']

todos = dict()

HELP = """
/help - вывести справку по программе.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - вывести все добавленные задачи.
/exit - выход из программы
/random - добавлять случайную задачу на дату Сегодня"""

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, f'Добрый день! Вы находитесь в программе ведения списка дел,\nСегодня {datetime.now().strftime("%d-%m-%Y")}')

def get_date(message): #получаем дату
    global date
    date = message.text
    return date

def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=["random"])
def random(message):
    task = choice(RANDOM_TASKS)
    date = datetime.now().strftime("%d-%m-%Y")
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=["show"])
def show(message):
    bot.send_message(message.chat.id, "Введите дату:")
    bot.register_next_step_handler(message, message.text)
    date = message.text
    print(date)
    if date in todos:
        tasks = ''
        for task in todos[date]:
            tasks += f' - {task}\n'
    else:
        tasks = "Такой даты нет"

    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)
