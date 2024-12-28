import unittest

from data_structures_and_algorithms.algorithms.backtracking.permutations.permute import get_permutations


class Test(unittest.TestCase):
    def test_permute(self):
        strings = [
            ('ABC', ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']),
            ('XY', ['XY', 'YX'])
        ]

        for string in strings:
            self.assertCountEqual(string[1], get_permutations(string[0]))
