import unittest

from data_structures_and_algorithms.algorithms.backtracking.permutations.permute import get_permutations


class Test(unittest.TestCase):
    def test_permute(self):
        strings = [
            ('', []),
            ('a', ['a']),
            ('ab', ['ab', 'ba']),
            ('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
            ('aa', ['aa', 'aa'])
        ]

        for string in strings:
            self.assertCountEqual(string[1], get_permutations(string[0]))
