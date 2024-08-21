#                   Потоки на классах
# Задача "За честь и отвагу!":

from threading import Thread
from time import sleep

def ending(days):
    match days:
        case 1:
            return 'день'
        case 2 | 3 | 4:
            return 'дня'
        case _:
            return 'дней'

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        self.enemies = 100
        self.days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            sleep(1)
            self.days += 1
            self.enemies -= min(self.enemies, self.power)
            print(f'{self.name} сражается {self.days} {ending(self.days)}, '
                  f'осталось {self.enemies} воинов. ')
        else:
            print(f'{self.name} одержал победу спустя {self.days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')


