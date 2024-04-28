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

    def test_print_inorder(self):
        print_inorder_traversal(self.root)
        print()
        # Expected: 4 2 5 1 6 3 7

    def test_print_preorder(self):
        print_preorder_traversal(self.root)
        print()
        # Expected: 1 2 4 5 3 6 7

    def test_print_postorder(self):
        print_postorder_traversal(self.root)
        print()
        # Expected: 4 5 2 6 7 3 1

    def test_print_levelorder(self):
        print_level_order_traversal(self.root)
        print()
        # Expected:

