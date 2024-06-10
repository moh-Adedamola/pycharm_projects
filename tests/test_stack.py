import unittest
from mystack import MyStack


class MyTestCase(unittest.TestCase):

    def test_stack_can_add_element(self):
        stack = MyStack()
        stack.add_to_stack("semicolon.africa")
        stack.add_to_stack("google.com")
        self.assertEqual(len(stack.stack), 2)  # add assertion here

    def test_stack_can_remove_last_in_element(self):
        s1 = MyStack()
        s1.add_to_stack("semicolon.africa")
        s1.add_to_stack("google.com")
        s1.add_to_stack("reuters.ng")
        s1.add_to_stack("x.com")

        self.assertEqual(len(self.s1.stack), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
