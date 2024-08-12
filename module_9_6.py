# Генераторы
# Задача


def all_variants(text):
    '''Возвращает перечень всех подпоследовательностей исходной строки:
    односимвольные, двусимвольные, трехсимвольные и т.д.
    '''
    for i in range(len(text)): #  количество символов
        for j in range(len(text) - i):
            yield text[j : j+i+1]


a = all_variants("abcd")
for i in a:
    print(i)
