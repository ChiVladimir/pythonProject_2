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
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    guests_vs_tables = {}
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *args):
        list_guests = list(args)
        list_tables = self.tables

        for i in range(len(list_tables)):
            thread_1 = list_guests[i]
            thread_1.start()
            Cafe.guests_vs_tables[list_tables[i]] = list_guests[i]
            print(f'{list_guests[i].name} сел(-а) за стол номер {list_tables[i].number}')
        if len(list_guests) > (len(list_tables) - len(list_tables)):
            for i in range((len(list_tables) - len(list_tables)), len(list_guests)):
                self.queue.put(guests[i])
                print(f'{list_guests[i].name} в очереди')

    def busy_table(self):
        for table in self.tables:
            print(table.guest)
            if table.guest is not None:
                return True

    def discuss_guests(self):
        print(self.queue.empty(), Cafe.busy_table(self))
        print(self.guests_vs_tables)
        while not (self.queue.empty()) or Cafe.busy_table(self):
            for table in self.tables:
                print (self.tables)
                if table.guest is not None and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if self.queue.empty() is not True and table.guest is None:
                    print(self.queue.empty(), table.guest)
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread_2 = table.guest
                    thread_2.start()
                    Cafe.guests_vs_tables[table.number] = table.guest.name


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
