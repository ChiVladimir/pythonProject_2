#Домашнее задание по теме "Методы Юнит-тестирования"
import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):

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

    def test_challenge_1(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.tournament.start()
        TournamentTest.all_results[1] = self.all_results

    def test_challenge_2(self):
        self.tournament = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        TournamentTest.all_results[2] = self.all_results

    def test_challenge_3(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        TournamentTest.all_results[3] = self.all_results


if __name__ == "__main__":

    unittest.main()
