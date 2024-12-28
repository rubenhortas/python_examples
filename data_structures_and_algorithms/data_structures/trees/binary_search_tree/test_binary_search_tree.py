import unittest

from binary_search_tree import BinarySearchTree


class Test(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(7)
        bst.insert(5)
        bst.insert(6)
        bst.insert(12)
        bst.insert(4)
        bst.insert(6)
        bst.insert(5)
        bst.insert(7)

        self.assertEqual(['4 (1)', '5 (2)', '6 (2)', '7 (2)', '12 (1)'], bst.get_inorder_traversal())
