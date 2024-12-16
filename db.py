import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
) 
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

#cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("newuser", "examp@gmail.com", "28"))
# Операция добавления данных в базу данных(БД)
   # for i in range(30):
#cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"newuser{i}", f"{i}examp@gmail.com", "28"))

# Операция обновления данных (БД)-
#cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser" ))

# Операция удаления данных из (БД)
#cursor.execute("DELETE FROM Users WHERE username = ?", "newuser")

connection.commit()
connection.close()