# Создание потоков
# Задача "Потоковая запись в файлы":

from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as fil:
        for i in range(word_count):
            fil.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()

time_delta = time_end - time_start
print(f'Работа потоков (обычная запись) {time_delta}')

time_start = datetime.now()

th1 = Thread(target=write_words, args=(10, 'example5.txt'))
th2 = Thread(target=write_words, args=(30, 'example6.txt'))
th3 = Thread(target=write_words, args=(200, 'example7.txt'))
th4 = Thread(target=write_words, args=(100, 'example8.txt'))

for i in (th1, th2, th3, th4):
    i.start()

for i in (th1, th2, th3, th4):
    i.join()

time_end = datetime.now()

time_delta = time_end - time_start
print(f'Работа потоков (потоковая запись) {time_delta}')


