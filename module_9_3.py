first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первая генераторная сборка
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Вторая генераторная сборка
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))
print(list(second_result))
