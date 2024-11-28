import unittest
import module_12_1
from module_12_2 import Runner, Tournament


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(module_12_1.RunnerTest):
    def setUp(self):
        super().setUp()
        self.is_frozen = False
        return ("...OK")

    @skip_if_frozen
    def test_walk(self):
        super().test_walk()

    @skip_if_frozen
    def test_run(self):
        super().test_run()

    @skip_if_frozen
    def test_challenger(self):
        super().test_challenger()


class TournamentTest(unittest.TestCase):
    all_results = {}

    def setUp(self):
        self.is_frozen = True
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @skip_if_frozen
    def test_first_tournament(self):  # Был test_usain_and_nick
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[1] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(len(results), 2)

    @skip_if_frozen
    def test_second_tournament(self):  # Был test_andrey_and_nick
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[2] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(len(results), 2)

    @skip_if_frozen
    def test_third_tournament(self):  # Был test_usain_andrey_and_nick
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[3] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(len(results), 3)


def run_tests():
    # Создаем загрузчик тестов
    loader = unittest.TestLoader()

    # Создаем объект TestSuite
    my_suite = unittest.TestSuite()

    # Добавляем тесты в my_suite
    my_suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    my_suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(my_suite)


if __name__ == '__main__':
    run_tests()
