# Многопроцессное программирование

import multiprocessing
import threading
import time
from threading import Thread, Event


#print('\nExample 1')
started_at = time.time()
counter = 0

def first_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print(f'The first changes counter {counter}')

def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print(f'The second changes counter {counter}')

if __name__ == '__main__':
    started_at = time.time()

# thread_1 = threading.Thread(target=first_worker, args=(10,))
# thread_2 = threading.Thread(target=second_worker, args=(5,))
# thread_1.start()
# thread_2.start()

    process_1 = multiprocessing.Process(target=first_worker, args=(10,))
    process_2 = multiprocessing.Process(target=second_worker, args=(15,))
    process_1.start()
    process_2.start()

    ended_at = time.time()
    print(f'Time: {(ended_at - started_at) * 1000} milliseconds')
