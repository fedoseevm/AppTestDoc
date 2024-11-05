
import unittest
import nwd


class TestNWD(unittest.TestCase):

    def test_nwd_positive_numbers(self):
        self.assertEqual(nwd(30, 12), 6)

    def test_nwd_prime_numbers(self):
        self.assertEqual(nwd(7, 13), 1)

    def test_nwd_with_zero(self):
        self.assertEqual(nwd(0, 5), 5)

    def test_nwd_equal_numbers(self):
        self.assertEqual(nwd(14, 14), 14)

    def test_nwd_large_numbers(self):
        self.assertEqual(nwd(123456, 789012), 12)