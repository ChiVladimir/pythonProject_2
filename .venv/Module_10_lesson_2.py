# Введение в потоки. Потоки на классах
import threading
import time
from threading import current_thread


class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print(f'>Stream {self.name} is started\n')
        self.timer(self.name, self.counter, self.delay)
        print(f'>Stream {self.name} is finished\n')

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'>Stream {self.name}: {time.ctime((time.time()))}\n')
            counter -= 1

thread1 = MyThread('thread_1', 5, 1)
thread2 = MyThread('thread_2', 3, 0.5)
thread1.start()
thread2.start()
