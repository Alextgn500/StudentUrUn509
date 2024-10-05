import math


# Родительский класс Figure
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = sides
        self.filled = False

        # Проверка количества сторон
        def __is_valid_sides(self, *new_sides):
            if (len(new_sides) == self.sides_count and
                    all(isinstance(side, int) and side > 0 for side in new_sides)):
                return True
            return False

    # Геттер для цвета
    def get_color(self):
        return self.__color

    # Проверка валидности цвета
    def __is_valid_color(self, r, g, b):
        return all(0 <= color <= 255 and isinstance(color, int) for color in (r, g, b))

    # Сеттер для цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Проверка валидности сторон
    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    # Геттер для сторон
    def get_sides(self):
        return self.__sides

    # Сеттер для сторон
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Метод для получения периметра
    def __len__(self):
        return sum(self.__sides)


# Класс Circle, наследуется от Figure
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    # Метод для получения площади круга
    def get_square(self):
        return math.pi * self.__radius ** 2


# Класс Triangle, наследуется от Figure
class Triangle(Figure):
    sides_count = 3

    # Метод для получения площади треугольника
    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Переименуем метод area в get_square для соответствия

    def area(self):
        return self.get_square()

    def print_area(self):
        area = self.get_square()  # Используем get_square вместо area
        print(f"Площадь треугольника со сторонами {self.get_sides()} равна {area:.2f}")

   # Класс Cube, наследуется от Figure
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            super().__init__(color, *([sides[0]] * 12))
        else:
            super().__init__(color, *sides)

    # Метод для получения объема куба
    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Код для проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади треугольника
def print_triangle_square():
    Triangle("red", 5, 5, 5).print_area()
    Triangle("blue", 3, 4, 5).print_area()
    Triangle("green", 7, 8, 9).print_area()

if __name__ == "__main__":
    print_triangle_square()


