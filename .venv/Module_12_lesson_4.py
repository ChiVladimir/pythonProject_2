# Систематизация тестов

import Module_12_lesson_3 as calc_test
import Module_12_lesson_3_2 as calc_test_new
import unittest

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(calc_test.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(calc_test_new.CalcTest))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(calcST)
