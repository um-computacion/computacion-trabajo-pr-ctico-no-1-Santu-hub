import unittest
from src.roman_converter import decimal_to_romano

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_romano(1), "I")
        self.assertEqual(decimal_to_romano(5), "V")
        self.assertEqual(decimal_to_romano(10), "X")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_romano(4), "IV")
        self.assertEqual(decimal_to_romano(9), "IX")
        self.assertEqual(decimal_to_romano(40), "XL")
        self.assertEqual(decimal_to_romano(90), "XC")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_romano(49), "XLIX")
        self.assertEqual(decimal_to_romano(99), "XCIX")
        self.assertEqual(decimal_to_romano(499), "CDXCIX")
        self.assertEqual(decimal_to_romano(999), "CMXCIX")
        self.assertEqual(decimal_to_romano(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()