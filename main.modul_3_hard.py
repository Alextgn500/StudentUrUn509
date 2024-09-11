def calculate_structure_sum(*args):
    total = 0

    def recursive_sum(item):
        nonlocal total
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, (list, tuple, set)):
            for element in item:
                recursive_sum(element)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)

    for arg in args:
        recursive_sum(arg)

    return total

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Выводит: 99
