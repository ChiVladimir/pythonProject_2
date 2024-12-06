#Домашнее задание по теме "Обзор сторонних библиотек Python"

# Пример 1
#«Необходимый минимум для web scraping (автоматизированный процесс извлечения данных с сайта)».

# BeautifulSoup - библиотека для парсинга HTML и XML документов в Python.
# Requests - это библиотека для языка Python, которая позволяет работать с HTTP-запросами.
# Fake_useragent - это библиотека на Python, которая позволяет генерировать и рандомизировать
# строки User-Agent (идентификационная строка клиентского приложения).
# Она помогает имитировать поведение реальных пользователей, снижать вероятность
# обнаружения и блокировки при веб-скрапинге.

from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
import os
from fake_useragent import UserAgent

# Нырок 1, в список
url_bgn = 'https://www.avito.ru/all/mall/zapchasti_i_aksessuary?q='
print("\nВНИМАНИЕ! Перед запуском модуля необходимо включить VPN\n")
url_end =  str(input('Введите запрос для поиска (вместо пробелов необходимо ввести +) >>>'))
url = url_bgn + url_end
print(url)
response = requests.get(url, headers={'User-Agent': UserAgent().safari})
soup = BeautifulSoup(response.text, 'lxml')
name = 'soup.txt'
file = open(name, 'a')
file.write(str(soup))
file.close()
item_item = soup.find_all("div", {"data-marker": "catalog-serp"})
name = 'item_item.txt'
file = open(name, 'a')
file.write(str(item_item))
file.close()
quest = str(item_item[0])

indexes = []
for match in re.finditer(r'data-item-id', quest):
    indexes.append(match.start())
print(indexes)

data_item_id = []
for i in range(len(indexes)):
    x=indexes[i]+14
    y = x + 10
    data_item_id.append(quest[x:y])
print(data_item_id)
name = 'data_item_id.txt'
with open(name, "w+") as fp:
    data_to_write = '\n'.join(data_item_id)
    file.write(data_to_write)
    file.close()

# Пример 2
#«Неуспешная попытка оптимизировать код на https://contest.yandex.ru/contest (оптимизация удачная - уменьшение
# времени на 50%)), но Яндекс при компиляции кода не дает возможности использовать библиотеки.
# Условие задачи:
# Рассчитать скользящее среднее для последовательности.
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
#
# Измерения велись n секунд. В секунду i поступает qi запросов.
#
# Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
# Input
# В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения.
#
# Во второй строке через пробел записаны n целых неотрицательных чисел(через пробел).
#
# В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.
# Output
# Выведите через пробел результат применения метода скользящего среднего к серии измерений.
# Должно быть выведено n - k + 1 элементов, каждый элемент -— вещественное (дробное) число.
"""
9
9 3 2 0 1 5 1 0 0
3
"""


# Стандартный код

set_1 = []
set_1_inp = []
time_in_sec = float
window_size = int
result = []

time_in_sec = float(input())
set_1 = list(map(int, input().split()))
window_size = int(input())

i = 0
j = 1 + len(set_1) - window_size

result = [str(sum(set_1[i: i + window_size]) / window_size) for i in range (0, j)]

print(*result, sep=' ')

# Код с использованием NumPy
# (NumPy (Numeric Python) — это библиотека для Python, которая работает с многомерными
# массивами и включает набор математических функций. Библиотека обеспечивает быстрые вычисления
# по сравнению с обычными структурами данных в Python.)

import numpy as np

def moving_average(a, n):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1 :] / n

set_1 = []
set_1_inp = []
time_in_sec = float
window_size = int
result = []

time_in_sec = float(input())
set_1 = list(map(int, input().split()))
window_size = int(input())

data = np.array(set_1)

print(*(moving_average(data, window_size)), sep=' ')

