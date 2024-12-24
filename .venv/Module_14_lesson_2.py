# Создание, Изменение и Удаление элементов БД
# Data-Base Setup

import sqlite3

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

#cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (27, 'newuser'))

#cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

connection.commit()
connection.close()