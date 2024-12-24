# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

import sqlite3
import random
from random import randint

from matplotlib.backend_tools import cursors

connection = sqlite3.connect("not_telegram.db", timeout=10)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)'
                   , (f'User_{i + 1}', f'example{i + 1}@gmail.com', (i + 1) * 10, 1000))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(f'{user[0]:2}, {user[1]}, {user[2]}, {user[3]}, {user[4]}')

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(f'{user[0]:2}, {user[1]}, {user[2]}, {user[3]}, {user[4]}')

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(f'{user[0]:2}, {user[1]}, {user[2]}, {user[3]}, {user[4]}')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age !=?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()