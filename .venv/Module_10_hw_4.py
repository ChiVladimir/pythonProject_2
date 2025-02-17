# Домашнее задание по теме
# "Очереди для обмена данными между потоками."
from queue import Queue
import time
import threading
from threading import Thread
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    guests_vs_tables = {}
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)


    def guest_arrival(self, *args):
        for guest in args:
            if self.non_busy_table() is not None:
                thread_1 = guest
                thread_1.start()
                table = self.non_busy_table()
                self.guests_vs_tables[table] = thread_1
                table.guest = thread_1
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def non_busy_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def discuss_guests(self):

        while not (self.queue.empty()) or Cafe.non_busy_table(self):
            for table in self.tables:

                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if self.queue.empty() is not True and table.guest is None:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        thread_2 = table.guest
                        thread_2.start()
                        Cafe.guests_vs_tables[table] = thread_2



# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria',
                'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
