from random import choice

# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x.lower() == y.lower(), first, second))
print(result)


# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for item in data_set:
                file.write(str(item) + '\n')
            # Данные успешно записаны в файл file_name
        for item in data_set:
            print(item)

    return write_everything


# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод call
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
