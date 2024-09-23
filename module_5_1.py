class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


# Создаем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to у объектов
print(f"Едем на 5 этаж в {h1.name}:")
h1.go_to(5)

print(f"\nПытаемся поехать на 10 этаж в {h2.name}:")
h2.go_to(10)

# Дополнительный пример
h3 = House('ЖК Эльбрус', 30)
print(f"\nЕдем на 3 этаж в {h3.name}:")
h3.go_to(3)
