# Создание БД и инициализация
# Data-Base Setup

import sqlite3

from matplotlib.backend_tools import cursors

connection = sqlite3.connect("Module_14_lesson_1_database.db")
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


connection.commit()
connection.close()