class Vehicle:
    __COLOR_VARIANTS = ["RED", "GREEN", "WHITE", "BLACK", "BLUE"]

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color.upper()
            print(f"Цвет успешно изменен на {new_color.upper()}")
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    __SEDAN_COLOR_VARIANTS = ['BLACK', 'WHITE', 'RED']

    def __init__(self, owner, model, color, engine_power):
        self.__sedan_owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.owner = "Vasyok"  # Переопределяем владельца

    def get_model(self):
        return f"Модель седана: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя седана: {self.__engine_power}"

    def get_color(self):
        return f"Цвет седана: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.__sedan_owner}")

    def set_color(self, new_color):
        color_found = False
        for color in self.__SEDAN_COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                color_found = True

        if color_found:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет седана на {new_color}")

    def set_sedan_owner(self, new_owner):
        self.__sedan_owner = new_owner

# Создаем объект класса Sedan
vehicle1 = Sedan("Федос", "Тойота Mark II ", "синий", 500)

# Выводим начальную информацию
print("Начальная информация:")
vehicle1.print_info()
print()

# Пытаемся изменить цвет
vehicle1.set_color('PINK')
vehicle1.set_color('BLACK')

# Меняем владельца седана
vehicle1.set_sedan_owner('Vasyok')

# Выводим обновленную информацию
print("Обновленная информация:")
vehicle1.print_info()
