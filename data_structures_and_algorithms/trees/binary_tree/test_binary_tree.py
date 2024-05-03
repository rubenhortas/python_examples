import unittest

from binary_tree import BinaryTree


class Test(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree()
        self.binary_tree.insert('1')
        self.binary_tree.insert('2')
        self.binary_tree.insert('3')
        self.binary_tree.insert('4')
        self.binary_tree.insert('5')
        self.binary_tree.insert('6')
        self.binary_tree.insert('7')
        self.inorder_traversal_expected_values = ['4', '2', '5', '1', '6', '3', '7']
        self.preorder_traversal_expected_values = ['1', '2', '4', '5', '3', '6', '7']
        self.postorder_traversal_expected_values = ['4', '5', '2', '6', '7', '3', '1']
        self.level_order_traversal_expected_values = ['1', '2', '3', '4', '5', '6', '7']
        self.level_order_traversal_spiral_expected_values = ['1', '2', '3', '7', '6', '5', '4']

    def test_print_inorder_traversal(self):
        self.assertEqual(self.inorder_traversal_expected_values, self.binary_tree.get_inorder_traversal())

    def test_print_preorder_traversal(self):
        self.assertEquals(self.preorder_traversal_expected_values, self.binary_tree.get_preorder_traversal())

    def test_print_postorder_traversal(self):
        self.assertEqual(self.postorder_traversal_expected_values, self.binary_tree.get_postorder_traversal())

    def test_print_level_order_traversal(self):
        self.assertEqual(self.level_order_traversal_expected_values, self.binary_tree.get_level_order_traversal())

    def test_delete_value(self):
        self.binary_tree.delete('5')
        self.assertEqual(['1', '2', '3', '4', '7', '6'],self.binary_tree.get_level_order_traversal())

    def test_delete_root(self):
        self.binary_tree.delete(str(self.binary_tree.root))
        self.assertEqual(['7', '2', '3', '4', '5', '6'], self.binary_tree.get_level_order_traversal())

    def test_delete_deepest_rightmost(self):
        self.binary_tree.delete('7')
        self.assertEqual(['1', '2', '3', '4', '5', '6'], self.binary_tree.get_level_order_traversal())

    def test_get_height(self):
        self.binary_tree.delete('7')
        self.assertEqual(3, self.binary_tree.get_height())

        self.binary_tree = BinaryTree()
        self.assertEqual(0, self.binary_tree.get_height())

    def test_get_lot_spiral(self):
        self.assertEqual(self.level_order_traversal_spiral_expected_values, self.binary_tree.get_lot_spiral())

    def test_get_lot_spiral_stacks(self):
        self.assertEqual(self.level_order_traversal_spiral_expected_values, self.binary_tree.get_lot_spiral_stacks())
