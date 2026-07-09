import unittest

from data_structures_and_algorithms.data_structures.trees.avl_tree.avl_tree import AvlTree


class Test(unittest.TestCase):
    def test_avl(self) -> None:
        avl = AvlTree()
        avl.insert_value(1)
        avl.insert_value(2)
        avl.insert_value(3)
        avl.insert_value(4)
        avl.insert_value(5)

        self.assertEqual([2, 1, 4, 3, 5], avl.preorder())

        avl.delete_value(2)
        self.assertEqual([3, 1, 4, 5], avl.preorder())
