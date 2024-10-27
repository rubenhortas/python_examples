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

    def test_avl(self):
        self.assertEqual([3, 2, 1, 4, 5], self.avl.preorder())

        self.avl.delete_value(2)
        self.assertEqual([3, 1, 5, 4], self.avl.preorder())
