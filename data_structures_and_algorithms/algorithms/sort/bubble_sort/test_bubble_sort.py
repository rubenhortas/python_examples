import unittest

from data_structures_and_algorithms.algorithms.sort.bubble_sort.bubble_sort import sort


class Test(unittest.TestCase):
    def test_sort(self):
        lists = [
            # (list, ascending_sorted_list, descending_sorted_list)
            ([], []),
            ([5], [5]),
            ([4, 4, 4, 4], [4, 4, 4, 4]),
            ([4, 2, 6, 3, 1], [1, 2, 3, 4, 6]),
            ([4, 2, 6, 3, 4, 6, 2, 1], [1, 2, 2, 3, 4, 4, 6, 6])
        ]

        for lst in lists:
            self.assertEqual(lst[1], sort(lst[0]))
