import sqlite3

# Подключение к БД
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Генерация данных для 10 пользователей
users_data = [
    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
    for i in range(1, 11)
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)


# Обновление balance для каждой второй записи
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

# Удаление каждой третьей записи
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

# Выборка записей где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

#Удаление пользователя с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчет общего количества записей в БД
cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
print(total1)

# Подсчет общего баланса всех пользователей
cursor.execute('SELECT SUM(balance) FROM Users')
total2 = cursor.fetchone()[0]
print(total2)

# Подсчет среднего баланса пользователя
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()