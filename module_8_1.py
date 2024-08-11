# Try и Except
# Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        c = a + b
        return round(c, 5)
    except TypeError:
        return str(a) + str(b)
    except Exception as errr:
        print('Какая-то ошибка ... ', errr, type(errr))


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


