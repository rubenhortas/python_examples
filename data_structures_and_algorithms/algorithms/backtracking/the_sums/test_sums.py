# Create a function that finds all combinations of numbers in a list that add up to the target value.
# The function will receive a list of positive integers and a target value.
# To obtain the combinations, each element of the list can only be used once (but there may be repeated elements in it).
# Example:
#   List = [1, 5, 3, 2], Target = 6
#   Solutions: [1, 5] and [1, 3, 2]
# If there are no combinations, return an empty list.

import unittest

from data_structures_and_algorithms.algorithms.backtracking.the_sums.sums import get_sums


class Combination:
    def __init__(self, numbers, target, solutions):
        self.numbers = numbers
        self.target = target
        self.solutions = solutions


class Test(unittest.TestCase):
    def setUp(self):
        self.combinations = []

        combination = Combination([1, 5, 3, 2], 6, [[1, 5], [1, 3, 2]])
        self.combinations.append(combination)

        combination = Combination([1, 7], 6, [])
        self.combinations.append(combination)

        combination = Combination([1, 7, 3, 2], 6, [[1, 3, 2]])
        self.combinations.append(combination)

        combination = Combination([1, 1, 1, 1, 1, 1], 6, [[1, 1, 1, 1, 1, 1]])
        self.combinations.append(combination)

    def test_sums(self):
        for combination in self.combinations:
            self.assertEqual(combination.solutions, get_sums(combination.numbers, combination.target))
