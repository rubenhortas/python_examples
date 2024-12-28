import unittest

from data_structures_and_algorithms.algorithms.shunting_yard.reverse_polish_notation import rpn_to_infix
from data_structures_and_algorithms.algorithms.shunting_yard.shunting_yard import shunting_yard


class Test(unittest.TestCase):
    def test_shunting_yard(self):
        infix_expressions = [
            ('1 + 2 * 3 + (4 + 5 * 6)', '1 2 3 * + 4 5 6 * + +'),
            ('11 + 22 * 33 + (44 + 55 * 66)', '11 22 33 * + 44 55 66 * + +')
        ]

        for expression, expected_result in infix_expressions:
            self.assertEquals(expected_result, shunting_yard(expression))

    def test_rpn_to_infix(self):
        rpn_expressions = [
            ('1 2 3 * + 4 5 6 * + +', '((1+(2*3))+(4+(5*6)))')
        ]

        for expression, expected_result in rpn_expressions:
            self.assertEquals(expected_result, rpn_to_infix(expression))
