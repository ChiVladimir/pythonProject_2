# Домашнее задание по теме
# "Потоки на классах"
import threading
import time
from threading import Thread



class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.enemy = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.counter(self.name, self.power, self.enemy)
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

    def counter(self, name, power, enemy):
        day = 0
        while enemy:
            time.sleep(1)
            enemy -= power
            day += 1
            print(f'{self.name} сражается {day} день(дня)..., осталось {enemy} воинов.\n')
        self.day = day


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print ('Все битвы закончились!')