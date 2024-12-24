# Выбор Элементов БД

import sqlite3
import random
from random import randint

from matplotlib.backend_tools import cursors

connection = sqlite3.connect("Module_14_lesson_1_myDB.db", timeout=7)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# cursor.execute('INSERT INTO Users (username, email, age) VALUES(?, ?, ?)'
#               , ('newuser', 'ex@gmail.com', '28'))

# for i in range(30):
#     cursor.execute('INSERT INTO Users (username, email, age) VALUES(?, ?, ?)'
#                    , (f'newuser_{i + 1}', f'{i + 1}_ex@gmail.com', str(random.randint(20, 50))))


# for i in range(3, 32):
#     cursor.execute('UPDATE Users SET age = ? WHERE id = ?', (str(random.randint(20, 50)), i))

#SELECT FROM WHERE GROUP BY HAVING ORDER BY

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute('SELECT username, age FROM Users WHERE age >=?', (30,))
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute('SELECT username, age FROM Users GROUP BY age')
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()