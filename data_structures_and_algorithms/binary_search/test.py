import unittest

from binary_search import locate_position


class Test(unittest.TestCase):
    def setUp(self):
        self.numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.numbers2 = [9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]

    def test_in_the_middle(self):
        result = locate_position(self.numbers, 4)
        self.assertEqual(result, 5)

    def test_is_first_element(self):
        result = locate_position(self.numbers, 9)
        self.assertEqual(result, 0)

    def test_is_last_element(self):
        result = locate_position(self.numbers, 0)
        self.assertEqual(result, 9)

    def test_is_the_only_number(self):
        result = locate_position([1], 1)
        self.assertEqual(result, 0)

    def test_not_in_list(self):
        result = locate_position(self.numbers, 11)
        self.assertEqual(result, -1)

    def test_empty_list(self):
        result = locate_position([], 1)
        self.assertEqual(result, -1)

    def test_repeated_numbers(self):
        result = locate_position(self.numbers2, 6)
        self.assertEqual(result, 9)

    def test_several_appearances(self):
        result = locate_position(self.numbers2, 4)
        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()  # Run all tests
