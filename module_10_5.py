from multiprocessing import Pool
import time
from datetime import datetime


def read_info(name):
    """
    Функция для чтения данных из файла
    """
    all_data = []  # Создаем локальный список
    with open(name, 'r') as file:  # Открываем файл для чтения
        line = file.readline()  # Читаем первую строку
        while line:  # Пока строка не пустая
            all_data.append(line)  # Добавляем строку в список
            line = file.readline()  # Читаем следующую строку


if __name__ == '__main__':
    # Создаем список имен файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # ЛИНЕЙНЫЙ ПОДХОД
    start_time = datetime.now()  # Засекаем время начала
    for file in filenames:
        read_info(file)
    end_time = datetime.now()  # Засекаем время окончания
    print(f'Линейное выполнение заняло: {end_time - start_time}')

    # МНОГОПРОЦЕССНЫЙ ПОДХОД
    start_time = datetime.now()  # Засекаем время начала

    # Используем контекстный менеджер для создания пула процессов
    with Pool() as pool:

        # Применяем функцию read_info ко всем файлам параллельно
        pool.map(read_info, filenames)

    end_time = datetime.now()  # Засекаем время окончания
    print(f'Многопроцессное выполнение заняло: {end_time - start_time}')
