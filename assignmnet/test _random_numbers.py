import unittest

from randomnumberslist import get_random_numbers


class MyTestCase(unittest.TestCase):
    def test_get_random_numbers(self):
        self.assertEqual(get_random_numbers(), [32, 18, 24, 41, 16, 45, 31, 50, 22, 6])  # add assertion here

    def test_find_length(self):
        self.assertEqual(get_random_numbers(), [32, 18, 24, 41, 16, 45, 31, 50, 22, 6],10)  # add assertion here


if __name__ == '__main__':
    unittest.main()
