def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для результатов
    results = {}

    # Перебираем все функции из *functions
    for func in functions:
        # Записываем в словарь results результат работы функции под ключом её названия
        results[func.__name__] = func(int_list)

    # Возвращаем словарь results
    return results


# Пример использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
