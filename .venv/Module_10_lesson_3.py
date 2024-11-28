# Проблемы многопоточного программирования, блокировки и обработка ошибок

import threading
import time
from typing import final

#from threading import Thread

counter = 0
lock = threading.Lock()
print(lock.locked())

def increment(name):
    global counter
    lock.acquire()
    for i in range(1000):
        counter += 1
        print(name, counter)
    lock.release()

def decrement(name):
    global counter
    with lock:
        for i in range(1000):
            counter -= 1
            print(name, counter)

thread1 = threading.Thread(target=increment, args=('thread_1',))
thread2 = threading.Thread(target=decrement, args=('thread_2',))
thread3 = threading.Thread(target=increment, args=('thread_3',))
thread4 = threading.Thread(target=decrement, args=('thread_4',))

thread1.start()
thread3.start()
thread2.start()
thread4.start()

# Через конструкцию try

def decrement_try(name):
    global counter
    try:
        lock.acquire()
        for i in range(1000):
            counter -= 1
            print(name, counter)
    except Exception:
        pass
    finally:
        lock.release()


thread5 = threading.Thread(target=decrement_try, args=('thread_5',))

thread5.start()