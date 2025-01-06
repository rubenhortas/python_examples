import unittest

from data_structures_and_algorithms.data_structures.stack.stack_left import StackLeft
from data_structures_and_algorithms.data_structures.stack.stack_right import StackRight


class Test(unittest.TestCase):
    def test_stack_left(self):
        stack = StackLeft()
        stack.append('First')
        stack.append('Second')
        stack.append('Third')
        # stack: ['Third', 'Second', 'First']

        stack.pop()
        self.assertEqual(['Second', 'First'], list(stack.queue))

        stack.pop()
        self.assertEqual(['First'], list(stack.queue))

    def test_stack_right(self):
        stack = StackRight()
        stack.append('First')
        stack.append('Second')
        stack.append('Third')
        # stack: ['First', 'Second', 'Third']

        stack.pop()
        self.assertEqual(['First', 'Second'], list(stack.queue))

        stack.pop()
        self.assertEqual(['First'], list(stack.queue))
