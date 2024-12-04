# Многопроцессное программирование

from queue import Queue
import time
from threading import Thread, Event


print('\nExample 1')

def first_worker():
    print('The first worker is begun his task')
    event.wait()
    time.sleep(5)
    print('The first worker is finished his task')

def second_worker():
    print('The second worker is begun his task')
    time.sleep(9)
    print('The second worker is finished his task')
    event.set()

event = Event()
thread_1 = Thread(target=first_worker)
thread_2 = Thread(target=second_worker)
thread_1.start()
thread_2.start()