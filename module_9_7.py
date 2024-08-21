# Декораторы
# Задача: Декораторы в Python


def is_prime(func): #  - декоратор

    def wrapper(*args): # - заменитель исходной функции
        summ = func(*args)
        print(f"{['Составное', 'Простое'][all(summ % i for i in range(2,summ//2))]}")
        return summ

    return wrapper

@is_prime
def sum_three(a, b, c): #  складывает 3 числа
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
