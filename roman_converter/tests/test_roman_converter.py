import sys
sys.path.append("..")

import unittest
from src.roman_converter import convert


class TestRomanConverter(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True)

    def test_one(self):
        self.assertEqual(convert("I"), 1)
