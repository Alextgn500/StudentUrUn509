def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if isinstance(a, (int, float)) and isinstance(b, str):
            return f"{a}{b}"
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return f"{a}{b}"
        else:
            raise TypeError("Аргументы должны быть одного типа (число или строка)")
    finally:()

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print("{:.3f}".format(123.456 + 7))
print('Файнали, процесс завершен')




