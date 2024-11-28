import unittest
import test_12_3cl

# Создаем объект TestSuite c его переменной my_suite
my_suite = unittest.TestSuite()
my_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_12_3cl.RunnerTest))
my_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_12_3cl.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_suite)
