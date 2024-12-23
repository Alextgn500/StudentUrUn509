import sqlite3
from texts14 import PRODUCTS


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INT NOT NULL,
        image_path TEXT NOT NULL
    );
    ''')

    cursor.executemany('INSERT INTO Products VALUES (?, ?, ?, ?, ?)', PRODUCTS)
    connection.commit()

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products


if __name__ == "__main__":
    initiate_db()
    print("База данных создана!")
