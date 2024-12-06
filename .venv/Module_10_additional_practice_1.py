# Дополнительная практика по модулю 10

# Многопроцессное программирование. Булки

import time
import random
from asyncio import timeout
from itertools import count
from threading import Thread
import queue

from setuptools.command.build import build


class Bulka(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            time.sleep(1)
            if random.random() > 0.9:
                self.queue.put('Подгорелая булка')
            else:
                self.queue.put('Нормальная булка')

class Kotleta(Thread):
    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):
        print(self.queue.qsize())
        while self.count:
#            bulka = self.queue.get()
            bulka = self.queue.get(timeout=2)
            if bulka == 'Нормальная булка':
                time.sleep(0.1)
                self.count -= 1
            print('Булок к приготовлению осталось: ', self.count)


queue = queue.Queue(maxsize=10)

t1 = Bulka(queue)
t2 = Kotleta(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()


