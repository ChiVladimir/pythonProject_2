# Очереди в потоках
from queue import Queue
import time
import threading


print('\nExample 1')

q = Queue()

q.put(5)

print(q.get(timeout=3))
print("End of program")

print('\nExample 2')

def getter(queue):
    while True: # not queue.empty():
        time.sleep(1)
        item = queue.get()
        print(f'Element {item} is got\n')

q = Queue(maxsize=10)
thread_1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread_1.start()

for i in range(10):
    time.sleep(3)
    q.put(i)
    print(f'Element {threading.current_thread()} was put, trial {i}.\n')




