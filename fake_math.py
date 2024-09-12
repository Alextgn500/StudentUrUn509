# fake_math.py

def divide(first, second):
    # Проверяем, не равен ли делитель нулю
    if second == 0:
        return 'Ошибка'
    # Если делитель не ноль, выполняем деление
    return first / second