# Определяем классы исключений
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

# Определяем основной класс Car
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        # Проверяем vin перед присваиванием
        if self.__is_valid_vin(vin):
            self.__vin = vin
        # Проверяем numbers перед присваиванием
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    # Приватный метод для проверки vin
    def __is_valid_vin(self, vin_number):
        # Проверяем, является ли vin целым числом
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        # Проверяем диапазон vin
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    # Приватный метод для проверки номеров
    def __is_valid_numbers(self, numbers):
        # Проверяем, является ли numbers строкой
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        # Проверяем длину номера
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

# Примеры использования
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
