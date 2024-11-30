import unittest
import logging
import traceback

# Настройка логирования с более подробным форматом
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
    encoding="UTF-8",
    format="%(asctime)s | %(levelname)s | %(message)s\n%(exc_info)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной и нулевой, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_speeds = [-5, -10, 0, 5]
        for speed in test_speeds:
            try:
                runner = Runner('TestRunner', speed=speed)
                for _ in range(10):  # Вызов для соответствия значению 50
                    runner.walk()
                self.assertEqual(runner.distance, 50)
                logging.info(f'"test_walk" выполнен успешно со скоростью {speed}')
            except ValueError as e:
                logging.warning(
                    f"Неверная скорость для Runner: {speed}",
                    exc_info=True)  # Добавляем вывод traceback

    def test_run(self):
        test_names = [123, 'Илья', True, 'Вася', {'name': 'test'}]
        for name in test_names:
            try:
                runner = Runner(name)
                for _ in range(10):
                    runner.run()
                self.assertEqual(runner.distance, 100)
                logging.info(f'"test_run" выполнен успешно с именем {name}')
            except TypeError as e:
                logging.warning(
                    f"Неверный тип данных для объекта Runner: {type(name).__name__}",
                    exc_info=True)  # Добавляем вывод traceback

    def test_challenger(self):
        runner1 = Runner('Runner1')
        runner2 = Runner('Runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

    if __name__ == '__main__':
        unittest.main()
