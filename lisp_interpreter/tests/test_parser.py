import sys

sys.path.append("..")

import unittest

from src.repl import parse


class TestParser(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True)

    def test_simple_string(self):
        actual = parse("ahi")
        expect = "ahi"
        self.assertEqual(actual, expect)

    def test_float_primitive(self):
        actual = parse("3.14")
        expect = 3.14
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
