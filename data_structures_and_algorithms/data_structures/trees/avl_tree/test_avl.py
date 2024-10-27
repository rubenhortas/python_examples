import unittest

from avl_tree import AvlTree


class Test(unittest.TestCase):
    def setUp(self):
        self.avl = AvlTree()
        self.avl.insert_value(1)
        self.avl.insert_value(2)
        self.avl.insert_value(3)
        self.avl.insert_value(4)
        self.avl.insert_value(5)
        self.expected_preorder = [2, 1, 4, 3, 5]

    def test_avl(self):
        self.assertEqual(self.expected_preorder, self.avl.preorder())
