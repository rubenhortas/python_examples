import unittest

from binary_search import locate_position


class Test(unittest.TestCase):

    def test_in_the_middle(self):
        result = locate_position([13, 11, 10, 7, 4, 3, 1, 0], 1)
        self.assertEquals(result, 6)

    def test_is_first_element(self):
        result = locate_position([4, 2, 1, -1], 4)
        self.assertEquals(result, 0)

    def test_is_last_element(self):
        result = locate_position([3, -1, -9, -127], -127)
        self.assertEquals(result, 3)

    def test_is_the_only_number(self):
        result = locate_position([6], 6)
        self.assertEquals(result, 0)

    def test_not_in_list(self):
        result = locate_position([9, 7, 5, 2, -9], 4)
        self.assertEquals(result, -1)

    def test_empty_list(self):
        result = locate_position([], 7)
        self.assertEquals(result, -1)

    def test_repeated_numbers(self):
        result = locate_position([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 3)
        self.assertEquals(result, 7)

    def test_several_appearances(self):
        result = locate_position([8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 6)
        self.assertEquals(result, 2)


if __name__ == '__main__':
    unittest.main()  # Run all tests
