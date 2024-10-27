"""
The AVL tree is a self–balancing binary search tree that guarantees the difference of the heights of the left and right subtrees of a node is at most 1.
"""

from node import Node


class AvlTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def _get_height(node):
        if not node:
            return 0

        return node.height

    @staticmethod
    def _get_min_value_node(node):
        current = node

        while current.left:
            current = current.left

        return current

    def _get_balance_factor(self, node):
        if not node:
            return 0

        return self._get_height(node.left) - self._get_height(node.right)

    def _insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if value > node.left.value:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        if balance_factor < -1:
            if value < node.right.value:
                node.right = self._rotate_right(node.right)

            return self._rotate_left(node)

        return node

    def _delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self._get_min_value_node(root.right)
            root.value = temp.value
            root.right = self._delete(root.right, temp.value)

        if not root:
            return root

        root._get_height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance_factor(root)

        if balance > 1 and self._get_balance_factor(root.left) >= 0:
            return self._rotate_right(root)

        if balance < -1 and self._get_balance_factor(root.right) <= 0:
            return self._rotate_left(root)

        if balance > 1 and self._get_balance_factor(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance < -1 and self._get_balance_factor(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _rotate_left(self, node):
        right_node = node.right
        temp = right_node.left

        right_node.left = node
        node.right = temp

        node._get_height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        right_node._get_height = 1 + max(self._get_height(right_node.left), self._get_height(right_node.right))

        return right_node

    def _rotate_right(self, node):
        left_node = node.left
        temp = left_node.right

        left_node.right = node
        node.left = temp

        node._get_height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        left_node._get_height = 1 + max(self._get_height(left_node.left), self._get_height(left_node.right))

        return left_node

    def _search(self, node, value):
        if not node or node.value == value:
            return node

        if node.value < value:
            return self._search(node.right, value)

        return self._search(node.left, value)

    def insert_value(self, value):
        self.root = self._insert(self.root, value)

    def delete_value(self, value):
        self.root = self._delete(self.root, value)

    def search_value(self, value):
        return self._search(self.root, value)

    def preorder(self):
        def traverse_preorder(node):
            if node:
                values.append(node.value)
                traverse_preorder(node.left)
                traverse_preorder(node.right)

        values = []
        traverse_preorder(self.root)
        return values
