import unittest
import calculator




class MyTestCase(unittest.TestCase):
    def test_suma(self):
        result = calculator.suma(10,20)
        self.assertEqual(result, 30)  # add assertion here
    def test_suma_neg(self):
        result = calculator.suma(-10,-20)
        self.assertEqual(result, -30)

class MyTestCase2(unittest.TestCase):
    def test_suma(self):
        result = calculator.suma(10,20)
        self.assertEqual(result, 30)  # add assertion here
    def test_suma_neg(self):
        result = calculator.suma(-10,-2)
        self.assertEqual(result, -12)

class MyTestCase3(unittest.TestCase):
    def test_srednia3(self):
        result = calculator.srednia3(15,10, 20)
        self.assertEqual(result, 15)  # add assertion here
    def test_srednia_neg(self):
        result = calculator.srednia3(-15,-10,-20)
        self.assertEqual(result, -15)

if __name__ == '__main__':
    unittest.main()