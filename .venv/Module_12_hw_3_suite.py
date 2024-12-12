#Домашнее задание по теме "Систематизация и пропуск тестов".

import Module_12_hw_3_tests as tests
import unittest


testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
