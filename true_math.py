# true_math.py

from math import inf

def divide(first, second):
    # Проверяем, не равен ли делитель нулю
    if second == 0:
        return inf
    # Если делитель не ноль, выполняем деление
    return first / second