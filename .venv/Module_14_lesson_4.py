# Функции в SQL запросах

import sqlite3
import random
from random import randint

from matplotlib.backend_tools import cursors

connection = sqlite3.connect("Module_14_lesson_1_myDB.db", timeout=7)
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users(
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# ''')
#
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')


cursor.execute('SELECT COUNT(*) FROM Users')
total1 = cursor.fetchone()[0]
total2 = cursor.fetchone()
total3 = cursor.fetchall()
print(total1)
print(total2)
print(total3)

cursor.execute('SELECT COUNT(*) FROM Users WHERE age > ?', (33,))
total4 = cursor.fetchone()[0]
print(total4)

cursor.execute('SELECT SUM(age) FROM Users')
total5 = cursor.fetchone()[0]
print(total5, total5 / total1)

cursor.execute('SELECT AVG(age) FROM Users')
total6 = cursor.fetchone()[0]
print(total6)

cursor.execute('SELECT MIN(age) FROM Users') #MAX(age)
total7 = cursor.fetchone()[0]
print(total7)




connection.commit()
connection.close()