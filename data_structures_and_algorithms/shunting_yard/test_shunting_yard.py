import unittest

from data_structures_and_algorithms.shunting_yard.reverse_polish_notation import rpn_to_infix
from data_structures_and_algorithms.shunting_yard.shunting_yard import shunting_yard


class Test(unittest.TestCase):
    def setUp(self):
        self.infix_expressions = [
            ('1 + 2 * 3 + (4 + 5 * 6)', '1 2 3 * + 4 5 6 * + +'),
            ('11 + 22 * 33 + (44 + 55 * 66)', '11 22 33 * + 44 55 66 * + +')
        ]

        self.rpn_expressions = [
            ('1 2 3 * + 4 5 6 * + +', '((1+(2*3))+(4+(5*6)))')
        ]

    def test_shunting_yard(self):
        for expression, result in self.infix_expressions:
            self.assertEquals(shunting_yard(expression), result)

    def test_rpn_to_infix(self):
        for expression, result in self.rpn_expressions:
            self.assertEquals(rpn_to_infix(expression), result)


if __name__ == '__main__':
    unittest.main()
