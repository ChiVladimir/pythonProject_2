# Асинхронность. Примеры

import time
import asyncio

print('Example 1')

def get_temp():
    print('The first indication')
    time.sleep(2)
    print('25 С degrees')

def get_press():
    print('The second indication')
    time.sleep(4)
    print('101 kPa')

def main():

#    task =  asyncio.create_task(notification())

    print('Start!')
    get_temp()
    get_press()
    print("Finish")

start = time.time()
main()
finnish = time.time()

print(f'Working time is {round(finnish - start, 2)} seconds')

print('Example 2')

async def get_temp_():
    print('The first indication')
    await asyncio.sleep(2)
    print('25 С degrees')

async def get_press_():
    print('The second indication')
    await asyncio.sleep(4)
    print('101 kPa')

async def main_():

#    task =  asyncio.create_task(notification())

    print('Start!')
    task1 = asyncio.create_task(get_temp_())
    task2 = asyncio.create_task(get_press_())
    await task1
    await task2
    print("Finish")

start = time.time()
asyncio.run(main_())
finnish = time.time()

print(f'Working time is {round(finnish - start, 2)} seconds')