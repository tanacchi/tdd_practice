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
