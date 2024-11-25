from primes import ifPrime
import unittest

class Test(unittest.TestCase):
    
    def test_zadanie1(self):
        result = ifPrime(7)
        self.assertEqual(result, True)

    def test_zadanie2(self):
        result = ifPrime(79)
        self.assertEqual(result, True)

    def test_zadanie3(self):
        result = ifPrime(42)
        self.assertEqual(result, False)

    def test_zadanie4(self):
        result = ifPrime(85)
        self.assertEqual(result, False)

    def test_zadanie5(self):
        result = ifPrime(-1)
        self.assertEqual(result, False)

    def test_zadanie6(self):
        result = ifPrime(-2)
        self.assertEqual(result, False)

    def test_zadanie7(self):
        result = ifPrime("a")
        self.assertEqual(result, False)

    def test_zadanie8(self):
        result = ifPrime(0.5)
        self.assertEqual(result, False)

    def test_zadanie9(self):
        result = ifPrime(0)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()