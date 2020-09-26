import sys
sys.path.append("..")

import unittest
from src.roman_converter import convert


class TestRomanConverter(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True)

    def test_one(self):
        self.assertEqual(convert("I"), 1)

    def test_two_and_three(self):
        self.assertEqual(convert("II"), 2)
        self.assertEqual(convert("III"), 3)

    def test_four(self):
        self.assertEqual(convert("IV"), 4)

    def test_five(self):
        self.assertEqual(convert("V"), 5)

    def test_six(self):
        self.assertEqual(convert("VI"), 6)

    def test_invalid_char(self):
        with self.assertRaises(ValueError):
            convert("K")

    def test_six(self):
        self.assertEqual(convert("VI"), 6)

    def test_nine(self):
        self.assertEqual(convert("IX"), 9)

    def test_ten(self):
        self.assertEqual(convert("X"), 10)

    def test_eleven(self):
        self.assertEqual(convert("XI"), 11)

    def test_fourty(self):
        self.assertEqual(convert("XL"), 40)

    def test_sixty(self):
        self.assertEqual(convert("LX"), 60)

    def test_ninety(self):
        self.assertEqual(convert("XC"), 90)

    def test_400(self):
        self.assertEqual(convert("CD"), 400)

    def test_900(self):
        self.assertEqual(convert("CM"), 900)

    def test_12(self):
        self.assertEqual(convert("XII"), 12)

    def test_24(self):
        self.assertEqual(convert("XXIV"), 24)

    def test_42(self):
        self.assertEqual(convert("XLII"), 42)

    def test_49(self):
        self.assertEqual(convert("XLIX"), 49)

    def test_89(self):
        self.assertEqual(convert("LXXXIX"), 89)

    def test_299(self):
        self.assertEqual(convert("CCXCIX"), 299)

    def test_493(self):
        self.assertEqual(convert("CDXCIII"), 493)

    def test_1960(self):
        self.assertEqual(convert("MCMLX"), 1960)

    def test_3999(self):
        self.assertEqual(convert("MMMCMXCIX"), 3999)
