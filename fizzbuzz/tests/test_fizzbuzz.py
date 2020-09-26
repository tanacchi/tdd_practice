import sys
sys.path.append("..")

import unittest
from src.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True)

    def test_one(self):
        expect = "1"
        actual = fizzbuzz(1)
        self.assertEqual(actual, expect)

    def test_two(self):
        expect = "2"
        actual = fizzbuzz(2)
        self.assertEqual(actual, expect)

    def test_three(self):
        expect = "Fizz"
        actual = fizzbuzz(3)
        self.assertEqual(actual, expect)

    def test_four(self):
        expect = "4"
        actual = fizzbuzz(4)
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
