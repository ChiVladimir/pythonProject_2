#Домашнее задание по теме "Систематизация и пропуск тестов".

from Module_12_hw_2 import Runner, Tournament
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_run(self):
        another_one_runner = Runner('Bob', 11)
        for _ in range(10):
            another_one_runner.run()
        self.assertEqual(another_one_runner.distance, 220)
    def test_walk(self):
        another_one_runner = Runner('Bob', 11)
        for _ in range(10):
            another_one_runner.walk()
        self.assertEqual(another_one_runner.distance, 110)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        another_one_runner = Runner('Bob', 11)
        another_one_runner_ = Runner('Rob', 11)
        for _ in range(10):
            another_one_runner.run()
            another_one_runner_.run()
        self.assertEqual(another_one_runner.distance, another_one_runner_.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for_print = dict(sorted(cls.all_results.items()))
        for value in for_print.values():
            for key, val in value.items():
                value[key] = str(val)
            print (value)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge_1(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.tournament.start()
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge_2(self):
        self.tournament = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge_3(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        TournamentTest.all_results[3] = self.all_results


if __name__ == "__main__":

    unittest.main()
