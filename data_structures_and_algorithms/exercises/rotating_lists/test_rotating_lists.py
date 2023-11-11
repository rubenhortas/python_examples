import unittest

from rotating_lists import calculate_rotations


class Test(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [0, 2, 3, 4, 5, 6, 9]
        self.lst1 = [5, 6, 9, 0, 2, 3, 4]
        self.lst1_rotations = 3
        self.lst2 = [6, 9, 0, 2, 3, 4, 5]
        self.lst2_rotations = 2
        self.lst3 = [4, 5, 6, 9, 0, 2, 3]
        self.lst3_rotations = 4
        self.lst4 = [4, 4, 5, 6, 6, 0, 2, 3]
        self.lst4_rotations = 5
        self.lst5 = [3, 3, 3, 4, 4, 5, 6, 6, 0, 2]
        self.lst5_rotations = 8
        self.one_element_list = [0]

    def test_empty_list(self):
        result = calculate_rotations([])
        self.assertEqual(0, result)

    def test_sorted_list(self):
        result = calculate_rotations(self.sorted_list)
        self.assertEqual(0, result)

    def test_one_element_list(self):
        result = calculate_rotations(self.one_element_list)
        self.assertEqual(result, 0)

    def test_list(self):
        result = calculate_rotations(self.lst1)
        self.assertEqual(self.lst1_rotations, result)

    def test_list2(self):
        result = calculate_rotations(self.lst2)
        self.assertEqual(self.lst2_rotations, result)

    def test_list3(self):
        result = calculate_rotations(self.lst3)
        self.assertEqual(self.lst3_rotations, result)

    def test_list4(self):
        result = calculate_rotations(self.lst4)
        self.assertEqual(self.lst4_rotations, result)

    def test_list5(self):
        result = calculate_rotations(self.lst5)
        self.assertEqual(self.lst5_rotations, result)


if __name__ == '__main__':
    unittest.main()  # Run all tests
