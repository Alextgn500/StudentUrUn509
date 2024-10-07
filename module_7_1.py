import pprint

class Product:
    """
    Класс, представляющий продукт в магазине.
    """
    def __init__(self, name, weight, category):
        """
        Инициализация объекта класса Product.
        :param name: название продукта (строка)
        :param weight: вес продукта (число)
        :param category: категория продукта (строка)
        """
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        """
        Возвращает строковое представление продукта в формате "название, вес, категория".
        """
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    """
    Класс, представляющий магазин с продуктами.
    """
    def __init__(self):
        """
        Инициализация объекта класса Shop.
        """
        self.__file_name = 'products.txt'

    def get_products(self):
        """
        Считывает всю информацию о продуктах из файла __file_name,
        закрывает файл и возвращает единую строку со всеми продуктами.
        """
        try:
            with open(self.__file_name, 'r') as f:
                products_str = f.read().strip()
        except FileNotFoundError:
            products_str = ''
        return products_str

    def add(self, *products):
        """
        Добавляет продукты в файл __file_name, если их там еще нет.
        :param products: список объектов класса Product
        """
        existing_products = self.get_products().split('\n')
        for product in products:
            if str(product) not in existing_products:
                with open(self.__file_name, 'a') as f:
                    f.write(str(product) + '\n')
                print(str(product))
            else:
                print(f"Продукт {product} уже есть в магазине")


# Пример использования
print("Первый запуск:")
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p2)

print(s1.get_products())

print("Второй запуск:")
s2 = Shop()
s2.add(p1, p2, p3)

print(s2.get_products())

print("\nСодержимое файла products.txt:")
with open(s1._Shop__file_name, 'r') as file:
     pprint.pprint(file.readlines())
