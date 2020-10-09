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


if __name__ == '__main__':
    unittest.main()
