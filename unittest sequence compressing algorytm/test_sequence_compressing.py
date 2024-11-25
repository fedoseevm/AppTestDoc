from sequence_compressing import compressTheSequence
import unittest

class Sequence_Compressing_Test(unittest.TestCase):

    def test_1(self):
        result = compressTheSequence("CCCTAAAACCGGGG")
        self.assertEqual(result, "3CT4A2C4G")

    def test_2(self):
        result = compressTheSequence("CTAG")
        self.assertEqual(result, "CTAG")

    def test_3(self):
        result = compressTheSequence("CTTTAAGAGAAT")
        self.assertEqual(result, "C3T2AGAG2AT")

    def test_4(self):
        result = compressTheSequence("")
        self.assertEqual(result, "")

    def test_5(self):
        result = compressTheSequence(None)
        self.assertEqual(result, "")

    def test_6(self):
        result = compressTheSequence("CCCCCC")
        self.assertEqual(result, "6C")

    def test_7(self):
        result = compressTheSequence("A")
        self.assertEqual(result, "A")

    def test_8(self):
        result = compressTheSequence("AB")
        self.assertEqual(result, "AB")



if __name__ == '__main__':
    unittest.main()