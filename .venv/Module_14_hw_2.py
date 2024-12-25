# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"

import sqlite3
import random
from random import randint

from matplotlib.backend_tools import cursors

connection = sqlite3.connect("not_telegram.db", timeout=10)
cursor = connection.cursor()

# Код из предыдущего задания
# Удаление пользователя с id=6

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчёт кол-ва всех пользователей

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()

