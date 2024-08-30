#                  Многопроцессное программирование
# Задача "Многопроцессное считывание":

from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name) as file:
        while s:= file.readline():
            all_data.append(s)

    return len(all_data)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# typp = 'линейный'
typp = 'многопроцессный'

#___________________________________________________________

# Линейный вызов

res = 0
if typp == 'линейный':

    time_start = datetime.now()

    for nm in filenames:
        res += read_info(nm)

    time_end = datetime.now()

    print(f'Считано: {res} строк')
    print(f'Time: {time_end - time_start} ({typp})')

#___________________________________________________________

# Многопроцессный

if typp == 'многопроцессный' and __name__ == '__main__':
    time_start = datetime.now()

    with Pool(processes = 4) as pool:
        res = sum(pool.map(read_info, filenames))

    time_end = datetime.now()

    print(f'Считано: {res} строк')
    print(f'Time: {time_end - time_start} ({typp})')

#___________________________________________________________
