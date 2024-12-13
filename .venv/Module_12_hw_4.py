# Домашнее задание по теме "Логирование"
import unittest
import logging
import rt_with_exceptions as tests
from rt_with_exceptions import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')

    def test_run(self):
        try:
            runner_1 = Runner(1000, 10)
            runner_2 = Runner('Bob', 10)
            runner_1.run()
            runner_2.run()
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
        logging.info(f'test_run" выполнен успешно')


    def test_walk(self):
        try:
            walker_1 = Runner('Rob', 10)
            walker_2 = Runner('Bob', -10)
            walker_1.walk()
            walker_2.walk()
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
        logging.info(f'test_walk" выполнен успешно')


    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        another_one_runner = Runner('Bob', 11)
        another_one_runner_ = Runner('Rob', 11)
        for _ in range(10):
            another_one_runner.run()
            another_one_runner_.run()
        self.assertEqual(another_one_runner.distance, another_one_runner_.distance)

if __name__ == "__main__":

    # logging.basicConfig(level=logging.INFO,
    #                     filemode='w',
    #                     filename='runner_tests.log',
    #                     format='%(asctime)s | %(levelname)s | %(message)s')

    unittest.main()

#     first = Runner('Вася', 10)
#     second = Runner('Илья', -5)
#     third = Runner('Арсен', 10)
# #
#     t = Tournament(101, first, second)
#     print(t.start())