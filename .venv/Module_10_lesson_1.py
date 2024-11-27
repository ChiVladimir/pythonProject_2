# Введение в потоки.
import threading
import time
from threading import current_thread


def func1():
    for i in range(10):
        time.sleep(1)

        print(i, threading.current_thread())

def func2(x):
    for i in range(10, 20):
        time.sleep(1)
        print(i, threading.current_thread())
        print(current_thread().is_alive())

thread = threading.Thread(target=func2, args=(1, ), daemon=True)
thread.start()
#thread.join()
print(current_thread().is_alive())
func1()


print(threading.current_thread())
print(threading.enumerate())
print(current_thread().is_alive())