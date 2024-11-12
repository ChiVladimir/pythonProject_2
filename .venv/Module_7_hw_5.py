# Домашнее задание по теме "Файлы в операционной системе".
import os
import time

directory = "First/Second/Third/Fourth/"

for root, dirs, files in os.walk(directory):
    os.chdir(directory)
    for file in files:
        filepath = os.path.join(directory + file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        current_directory = os.getcwd()
        parent_dir = os.path.dirname((current_directory))
        print(f'Обнаружен файл: {file},\nПуть: {filepath},'
              f'\nРазмер: {filesize} байт,\nВремя изменения: {formatted_time},'
              f'\nРодительская директория: {parent_dir}\n')
