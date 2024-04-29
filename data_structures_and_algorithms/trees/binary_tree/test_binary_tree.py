import unittest

from binary_tree import *


class Test(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.binary_tree = BinaryTree(self.root)
        self.inorder_traversal_expected_values = ['4', '2', '5', '1', '6', '3', '7']
        self.preorder_traversal_expected_values = ['1', '2', '4', '5', '3', '6', '7']
        self.postorder_traversal_expected_values = ['4', '5', '2', '6', '7', '3', '1']
        self.levelorder_traversal_expected_values = ['1', '2', '3', '4', '5', '6', '7']

    def test_print_inorder_traversal(self):
        self.assertEqual(self.binary_tree.get_inorder_traversal(), self.inorder_traversal_expected_values)

    def test_print_preorder_traversal(self):
        self.assertEquals(self.binary_tree.get_preorder_traversal(), self.preorder_traversal_expected_values)

    def test_print_postorder_traversal(self):
        self.assertEqual(self.binary_tree.get_postorder_traversal(), self.postorder_traversal_expected_values)

    def test_print_levelorder_traversal(self):
        self.assertEqual(self.binary_tree.get_level_order_traversal(), self.levelorder_traversal_expected_values)
