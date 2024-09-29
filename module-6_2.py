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

    def __init__(self, owner, model, color, engine_power):
        Vehicle.__init__(self, owner, model, color, engine_power)

# Пример использования
vehicle1 = Sedan("Fedos", "Toyota Mark II", "BLUE", 500)

print("Начальная информация:")
vehicle1.print_info()

print("\nПопытка изменить цвет на Pink:")
vehicle1.set_color('Pink')

print("\nИзменение цвета на BLACK:")
vehicle1.set_color('BLACK')

print("\nИзменение владельца на Vasyok")
vehicle1.owner = 'Vasyok'

print("\nОбновленная информация:")
vehicle1.print_info()

print("\nПопытка изменить цвет на RED:")
vehicle1.set_color('RED')

print("\nФинальная информация:")
vehicle1.print_info()
