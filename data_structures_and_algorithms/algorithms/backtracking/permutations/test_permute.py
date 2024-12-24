import unittest

from data_structures_and_algorithms.algorithms.backtracking.permutations.permute import get_permutations


class Test(unittest.TestCase):
    def setUp(self):
        self.strings = [
            ('ABC', ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']),
            ('XY', ['XY', 'YX'])
        ]

    def test_permute(self):
        for string in self.strings:
            self.assertCountEqual(string[1], get_permutations(string[0]))
