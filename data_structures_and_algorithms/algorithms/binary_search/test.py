# Write a program to find the position of a given number in a list of numbers arranged in **decreasing** order.
# Minimize the number of times we access elements from the list.

import unittest

from binary_search import get_position


class Test(unittest.TestCase):
    def setUp(self):
        self.numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.numbers2 = [9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]

    def test_get_middle_position(self):
        result = get_position(self.numbers, 4)
        self.assertEqual(5, result)

    def test_get_first_element(self):
        result = get_position(self.numbers, 9)
        self.assertEqual(0, result)

    def test_get_last_element(self):
        result = get_position(self.numbers, 0)
        self.assertEqual(9, result)

    def test_get_the_only_number(self):
        result = get_position([1], 1)
        self.assertEqual(0, result)

    def test_not_in_list(self):
        result = get_position(self.numbers, 11)
        self.assertEqual(-1, result)

    def test_empty_list(self):
        result = get_position([], 1)
        self.assertEqual(-1, result)

    def test_repeated_numbers(self):
        result = get_position(self.numbers2, 6)
        self.assertEqual(9, result)

    def test_several_appearances(self):
        result = get_position(self.numbers2, 4)
        self.assertEqual(13, result)
