#!/usr/bin/env python3

import unittest

from data_structures_and_algorithms.data_structures.trees.n_ary_tree.n_ary_tree import NAryTree


class TestNAryTree(unittest.TestCase):
    def setUp(self) -> None:
        # Structure:
        #        1
        #     /  |  \
        #    2   3   4
        #   / \
        #  5   6
        self.tree: NAryTree[int] = NAryTree(1)
        self.tree.insert(2, parent_value=1)
        self.tree.insert(3, parent_value=1)
        self.tree.insert(4, parent_value=1)
        self.tree.insert(5, parent_value=2)
        self.tree.insert(6, parent_value=2)

    def test_insert_and_find(self) -> None:
        node = self.tree.find(5)
        self.assertIsNotNone(node)
        self.assertTrue(node is not None)
        self.assertEqual(node.value, 5)
        self.assertEqual(node.parent.value if node.parent else None, 2)

    def test_delete_leaf_node(self) -> None:
        result = self.tree.delete(5)
        self.assertTrue(result)
        self.assertIsNone(self.tree.find(5))
        parent = self.tree.find(2)
        self.assertTrue(parent is not None)
        self.assertEqual(len(parent.children), 1)

    def test_delete_subtree(self) -> None:
        result = self.tree.delete(2)
        self.assertTrue(result)
        self.assertIsNone(self.tree.find(2))
        self.assertIsNone(self.tree.find(5))
        self.assertIsNone(self.tree.find(6))

    def test_traverse_preorder(self) -> None:
        values = [node.value for node in self.tree.traverse_preorder()]
        self.assertEqual(values, [1, 2, 5, 6, 3, 4])

    def test_traverse_postorder(self) -> None:
        values = [node.value for node in self.tree.traverse_postorder()]
        self.assertEqual(values, [5, 6, 2, 3, 4, 1])

    def test_traverse_inorder(self) -> None:
        values = [node.value for node in self.tree.traverse_inorder()]
        self.assertEqual(values, [5, 2, 6, 1, 3, 4])

    def test_traverse_level_order(self) -> None:
        values = [node.value for node in self.tree.traverse_level_order()]
        self.assertEqual(values, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
