#Домашнее задание по теме "Обзор сторонних библиотек Python"

# Пример 1
#«Необходимый минимум для web scraping (автоматизированный процесс извлечения данных с сайта)».

# BeautifulSoup - библиотека для парсинга HTML и XML документов в Python.
# Requests - это библиотека для языка Python, которая позволяет работать с HTTP-запросами.
# Fake_useragent - это библиотека на Python, которая позволяет генерировать и рандомизировать
# строки User-Agent (идентификационная строка клиентского приложения).
# Она помогает имитировать поведение реальных пользователей, снижать вероятность
# обнаружения и блокировки при веб-скрапинге.
# lxml — это высокопроизводительная, качественная библиотека для парсинга HTML и XML,
# сочетает скорость и полноту функций XML этих библиотек с простотой интерфейса, характерного для Python.
# lxml способна обрабатывать большие объемы данных XML.
# Re — это модуль в Python для работы с регулярными выражениями. Он позволяет искать, изменять или
# извлекать информацию из строк на основе шаблонов.


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
try:
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
except IndexError:
    print('Что-то пошло не так! Проверьте вызов сайта и проверьте файл soup.txt, нет ли Capcha. Возможно сменился формат, обратитесь к разработчику.')
