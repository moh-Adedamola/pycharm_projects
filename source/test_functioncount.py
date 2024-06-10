import unittest

from functioncount import find_length


class MyTestCase(unittest.TestCase):

    def test_find_length(self):
        self.assertEqual(find_length("proportion"), 10)


if __name__ == '__main__':
    unittest.main()
