import unittest
import nwd


class NWD_TestCase(unittest.TestCase):

    def test_nwd_both_positive(self):
        result = nwd.nwd(30, 12)
        self.assertEqual(result, 6)

    def test_nwd_both_negative(self):
        result = nwd.nwd(-14, -35)
        self.assertEqual(result, -7)

    def test_nwd_same_numbers(self):
        result = nwd.nwd(9, 9)
        self.assertEqual(result, 9)

    def test_nwd_prime_numbers(self):
        result = nwd.nwd(7, 13)
        self.assertEqual(result, 1)

    def test_nwd_zero_and_positive(self):
        result = nwd.nwd(0, 15)
        self.assertEqual(result, 15)
    
    def test_nwd_zero_and_negative(self):
        result = nwd.nwd(-18, 0)
        self.assertEqual(result, -18)

    def test_nwd_large_numbers(self):
        result = nwd.nwd(789012, 123456)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()