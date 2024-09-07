def get_multiplied_digits(number):
    # Преобразуем число в строку для удобства работы с отдельными цифрами
    str_number = str(number)

    # Получаем первую цифру числа и преобразуем ее обратно в целое число
    first = int(str_number[0])

    # Проверяем, осталось ли что-то после первой цифры
    if len(str_number) > 1:
        # Если да, то умножаем первую цифру на результат рекурсивного вызова функции
        # для оставшейся части числа
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если нет, то возвращаем только первую (и единственную) цифру
        return first


# Пример использования функции
result = get_multiplied_digits(40203)
print(result)
