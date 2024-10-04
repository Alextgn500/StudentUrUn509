class Vehicle:
    __COLOR_VARIANTS = ["RED", "GREEN", "WHITE", "BLACK", "BLUE"]

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color.upper()

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
            return {new_color.upper()}
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    def set_owner(self, new_owner):
        self.owner = new_owner



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

    def print_info(self):
        super().print_info()


    # Создаем объект класса Sedan
vehicle1 = Sedan("Федос", "Тойота Mark II", "BLUE", 500)

# Выводим начальную информацию
print("Начальная информация:")
vehicle1.print_info()
print()

# Пытаемся изменить цвет
result1 = vehicle1.set_color('PINK')
result2 = vehicle1.set_color('BLACK')

# Меняем владельца седана
vehicle1.set_owner('Vasyok')

# Выводим обновленную информацию
print("\nОбновленная информация:")
vehicle1.print_info()
