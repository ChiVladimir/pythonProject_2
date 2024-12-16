# Асинхронность. Понятия

import time
import asyncio



async def notification():
    time.sleep(10)
    print('Time before delivery is 10 min')


async def main():

    task =  asyncio.create_task(notification())

    print('We are going on a trip')
    print("We're eating")

asyncio.run(main())