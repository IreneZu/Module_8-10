#                                  Блокировки и обработка ошибок
# Задача "Банковские операции":

# race_condition

from threading import Thread, Lock
from random import randint, seed
from time import sleep

seed(1)

cnt = 100
class Bank:
    def __init__(self, balance = 0):
        self.balance = 0
        self.lock = Lock()
        self.cnt_plus = 0

    def deposit(self):
        for i in range(cnt):
            self.cnt_plus += 1
            iplus = randint(50, 500)
            self.balance += iplus
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение №{i+1}: {iplus}. Баланс: {self.balance} ', end='\n')

            sleep(0.001)


    def take(self):#
        i = 0
        while i < cnt:
            iminus = randint(50, 500)

            if iminus <= self.balance:

                i += 1
                self.balance -= iminus
                print(f'Запрос на {iminus} \n'
                      f'Снятие №{i}: {iminus}. Баланс: {self.balance} ')

            else:
                print(f'Запрос на {iminus} ')
                print(f'Запрос отклонён, недостаточно средств')

                if self.cnt_plus == cnt and self.balance < 60:
                    break
                self.lock.acquire(timeout=2)

            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
# th1.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
