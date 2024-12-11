# Идея Простые Юнит-тесты
# Framework UNITTEST

import Module_12_lesson_1 as calc
import unittest

class CalcTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_add_(self):
        self.assertEqual(calc.add(1, 2), 3) # ->  self.assertEqual(calc.add_ for wrong test

    def test_sub(self):
        self.assertEqual(calc.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 2), 6)

    def test_div(self):
        self.assertEqual(calc.div(10, 2), 5)





if __name__ == "__main__":
    unittest.main()