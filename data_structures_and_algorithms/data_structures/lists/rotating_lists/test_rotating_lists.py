# You are given a list of numbers, obtained by rotating a sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original **sorted list** was rotated to obtain the given list.
# Your function should have the worst-case complexity of **O(log(n))**.
# You can assume that **all the numbers in the list are unique**.
# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] three times.

import unittest

from rotating_lists import calculate_rotations


class Test(unittest.TestCase):
    def setUp(self):
        self.lists = [
            ([0, 2, 3, 4, 5, 6, 9], 0),
            ([5, 6, 9, 0, 2, 3, 4], 3),
            ([6, 9, 0, 2, 3, 4, 5], 2),
            ([4, 5, 6, 9, 0, 2, 3], 4),
            ([4, 4, 5, 6, 6, 0, 2, 3], 5),
            ([3, 3, 3, 4, 4, 5, 6, 6, 0, 2], 8),
            ([0], 0)
        ]

    def test(self):
        for lst in self.lists:
            rotations = calculate_rotations(lst[0])
            self.assertEqual(lst[1], rotations)
