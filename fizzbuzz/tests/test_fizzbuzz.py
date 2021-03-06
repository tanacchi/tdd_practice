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

    def test_multiple_of_3(self):
        actual = [fizzbuzz(i) for i in range(3, 100, 3) if i % 15 != 0]
        expect = ["Fizz"] * len(actual)
        self.assertListEqual(actual, expect)

    def test_multiple_of_5(self):
        actual = [fizzbuzz(i) for i in range(5, 100, 5) if i % 15 != 0]
        expect = ["Buzz"] * len(actual)
        self.assertListEqual(actual, expect)

    def test_multiple_of_15(self):
        actual = [fizzbuzz(i) for i in range(15, 100, 15)]
        expect = ["FizzBuzz"] * len(actual)
        self.assertListEqual(actual, expect)

    def test_from_1_to_15(self):
        expect = ["1", "2", "Fizz",
                  "4", "Buzz", "Fizz",
                  "7", "8", "Fizz",
                  "Buzz", "11", "Fizz",
                  "13", "14", "FizzBuzz"]
        actual = [fizzbuzz(i) for i in range(1, 16)]
        self.assertListEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
