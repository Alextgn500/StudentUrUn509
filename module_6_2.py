class Vehicle:
    COLOR_VARIANTS = ["RED", "GREEN", "WHITE", "BLACK", "BLUE"]

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color

    def get_model(self):
        return f"Модель: {self._model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self._engine_power}"

    def get_color(self):
        return f"Цвет: {self._color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
       #print(self.owner)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        Vehicle.__init__(self, owner, model, color, engine_power)
        self.__sedan_owner = owner

    def print_info(self):
        Vehicle.print_info(self)
        print(f"Владелец седана: {self.__sedan_owner}")

    def set_sedan_owner(self, new_owner):
        self.__sedan_owner = new_owner
        self.owner = new_owner

    def set_color(self, new_color):
        if new_color.upper() in self.COLOR_VARIANTS:
            self._color = new_color.upper()
            print(f"Цвет седана успешно изменен на {new_color.upper()}")
        else:
            print(f"Нельзя сменить цвет седана на {new_color}")


# Создаем объект класса Sedan
vehicle1 = Sedan("Федос", "Тойота Mark II", "синий", 500)

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
