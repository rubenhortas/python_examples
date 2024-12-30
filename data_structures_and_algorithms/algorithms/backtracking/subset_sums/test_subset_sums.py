# Create a function that finds all combinations of numbers in a list that add up to the target value.
# The function will receive a list of positive integers and a target value.
# To obtain the combinations, each element of the list can only be used once (but there may be repeated elements in it).
# Example:
#   List = [1, 5, 3, 2], Target = 6
#   Solutions: [1, 5] and [1, 3, 2]
# If there are no combinations, return an empty list.

import unittest

from data_structures_and_algorithms.algorithms.backtracking.subset_sums.subset_sums import get_subsets


class NumberSet:
    def __init__(self, numbers, target, solutions):
        self.numbers = numbers
        self.target = target
        self.solutions = solutions


class Test(unittest.TestCase):
    def test_get_subsets(self):
        number_sets = []

        number_set = NumberSet([1, 5, 3, 2], 6, [[1, 5], [1, 2, 3]])
        number_sets.append(number_set)

        number_set = NumberSet([1, 7], 6, [])
        number_sets.append(number_set)

        number_set = NumberSet([1, 7, 3, 2], 6, [[1, 2, 3]])
        number_sets.append(number_set)

        number_set = NumberSet([1, 1, 1, 1, 1, 1], 6, [[1, 1, 1, 1, 1, 1]])
        number_sets.append(number_set)

        number_set = NumberSet([1, 2, 1, 1, 1, 1, 2, 1], 6, [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2]])
        number_sets.append(number_set)

        for number_set in number_sets:
            self.assertCountEqual(number_set.solutions, get_subsets(number_set.numbers, number_set.target))
