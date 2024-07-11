import unittest

from binary_search_tree import BinarySearchTree


class Test(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(7)
        self.bst.insert(5)
        self.bst.insert(6)
        self.bst.insert(12)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(5)
        self.bst.insert(7)

    def test_insert(self):
        self.assertEqual(['4 (1)', '5 (2)', '6 (2)', '7 (2)', '12 (1)'], self.bst.get_inorder_traversal())
