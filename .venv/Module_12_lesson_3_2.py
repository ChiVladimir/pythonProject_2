# Методы Юнит-тестирования

import Module_12_lesson_1 as calc
import unittest
import random

class CalcTest(unittest.TestCase):
    def setUp(self):
        print('Setup')

    @classmethod
    def setUpClass(cls):
        print('Mega Setup')

    def tearDown(self):
        print('Shutup')

    @classmethod
    def tearDownClass(cls):
        print('Mega Shutup')

    @unittest.skip('Производится в другом кейсе')
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    @unittest.skip('Производится в другом кейсе')
    def test_add_(self):
        self.assertNotEqual(calc.add_(1, 2), 3)

    @unittest.skip('Производится в другом кейсе')
    def test_sub(self):
        self.assertEqual(calc.sub(5, 2), 3)

    @unittest.skip('Производится в другом кейсе')
    def test_mul(self):
        self.assertEqual(calc.mul(3, 2), 6)

    def test_div(self):
        self.assertEqual(calc.div(10, 2), 5)

    def test_test_1(self):
        self.assertTrue(True)

    def test_test_2(self):
        self.assertFalse(False)

    def test_test_3(self):
        self.assertIsNotNone(self, calc.none_)

    @unittest.skipIf(True,'Не повезло')
    def test_test_4(self):
        self.assertIn('a', 'self, calc.none_')

    def test_test_5(self):
        self.assertRaises(TypeError, 3)

    @unittest.skip('Производится в другом кейсе')
    def test_test_6(self):
        a = 2
        b = 2
        self.assertAlmostEqual(a, b)


if __name__ == "__main__":
    a = 2
    b = 2

    unittest.main()