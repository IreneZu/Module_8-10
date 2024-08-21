#                              Очереди для обмена данными между потоками
# Задача "Потоки гостей в кафе":

from threading import Thread, Lock
from random import randint, seed
from time import sleep
from queue import Queue


# seed(1)

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.gender = 'f' if (name.endswith('a') and name not in ('Nikita', 'Ilya')) else 'm'


    def run(self):
        sleep(randint(3, 10))

def ending(word, gen):
    if gen == 'm':
        return word
    else:
        match word:
            case 'сел' | 'покушал':
                return word + 'а'
            case 'ушёл':
                return 'ушла'
            case 'вышел':
                return 'вышла'


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} {ending("сел",guest.gender)} за стол номер {table.number}')

                    break


            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

        # [guest.join() for guest in guests if guest.is_alive()]


    def discuss_guests(self):

        while any(x.guest for x in tables):

            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f'{t.guest.name} {ending("покушал",t.guest.gender)} и {ending("ушёл",t.guest.gender)}')
                    print(f'Стол номер {t.number} свободен')
                    t.guest = None

                    if not self.queue.empty():
                        t.guest = self.queue.get()
                        print(f'{t.guest.name} {ending("вышел",t.guest.gender)} из очереди и {ending("сел",t.guest.gender)} за стол номер {t.number}')
                        t.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
