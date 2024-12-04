# Домашнее задание по теме
# "Многопроцессное программирование"

import time
from multiprocessing import Pool
import multiprocessing

def read_info(file_name):
    all_data = []
    f = open(file_name, "r")
    step = f.readlines()
    all_data = [all_data.append(step[i])for i in range(0, len(step))]

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

# started_at = time.time()
# for filename in filenames:
#     read_info(filename)
# ended_at = time.time()
# print(f'Линейный вызов: {round(ended_at - started_at, 4)} sec')



# Многопроцессный

# if __name__ == '__main__':
#     started_at = time.time()
#     with multiprocessing.Pool(processes=len(filenames)) as pl:
#         pl.map(read_info, filenames)
#     ended_at = time.time()
#     print(f'Многопроцессный вызов: {round(ended_at - started_at, 4)} sec')