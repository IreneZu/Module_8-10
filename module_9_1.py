# Введение в функциональное программирование
# Задание "Вызов разом"

def apply_all_func(int_list, *fuctions):
    # results = dict()
    results = {func.__name__ : func(int_list) for func in fuctions}
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))



