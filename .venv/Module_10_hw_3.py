# Домашнее задание по теме
# "Блокировки и обработка ошибок"
import threading
import time
import random
from threading import Thread
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            income = random.randint(50, 500)
            self.balance += income
            time.sleep(0.001)
            print(f'Пополнение: {income}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        for j in range(100):
            outcome = random.randint(50, 500)
            print(f'Запрос на {outcome}')
            if outcome <= self.balance:
                self.balance -= outcome
                print(f'Снятие: {outcome}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

