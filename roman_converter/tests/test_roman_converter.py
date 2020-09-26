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

