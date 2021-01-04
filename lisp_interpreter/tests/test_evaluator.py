import sys

sys.path.append("..")

import unittest

from src.repl import evaluate


class TestEvaluator(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True)

    def test_int_primitive(self):
        actual = evaluate(42)
        expected = 42
        self.assertEqual(actual, expected)

    def test_addition(self):
        actual = evaluate(['+', 5, 2])
        expected = 7
        self.assertEqual(actual, expected)

    def test_subtraction(self):
        actual = evaluate(['-', 9, 2])
        expected = 7
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
