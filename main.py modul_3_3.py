def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")

# 1. Вызовы функции с разным количеством аргументов
print("1. Вызовы функции с разным количеством аргументов:")
print_params()
print_params(2)
print_params(2, 'новая строка')
print_params(2, 'новая строка', False)
print_params(b=25)
print_params(c=[1,2,3])

# 2. Распаковка параметров
print("\n2. Распаковка параметров:")
values_list = [10, 'список', False]
values_dict = {'a': 100, 'b': 'словарь', 'c': [True, False]}

print("Распаковка списка:")
print_params(*values_list)

print("Распаковка словаря:")
print_params(**values_dict)

# 3. Распаковка + отдельные параметры
print("\n3. Распаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

# Пример безопасного использования изменяемого типа данных в качестве параметра по умолчанию
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    return list_my

print("\nПример безопасного использования списка:")
print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3, [10, 20]))
