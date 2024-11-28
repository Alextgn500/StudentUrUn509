import unittest
import module_12_1
import module_12_2

# Создание объекта TestSuite и присвоение его переменной  произвольного названия
my_test_suite = unittest.TestSuite()
my_test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
my_test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_test_suite)
