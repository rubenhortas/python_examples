"""
The AVL tree is a self–balancing binary search tree that guarantees the difference of the heights of the left and right subtrees of a node is at most 1.
"""

from node import Node


class AvlTree:
    def __init__(self):
        self.root = None

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

    def _delete(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        if not node:
            return node

        node._get_height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        balance = self._get_balance_factor(node)

        if balance > 1:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        if balance < -1:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)

            return self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        right_node = node.right
        temp = right_node.left

        right_node.left = node
        node.right = temp

        node._get_height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        right_node._get_height = max(self._get_height(right_node.left), self._get_height(right_node.right)) + 1

        return right_node

    def _rotate_right(self, node):
        left_node = node.left
        temp = left_node.right

        left_node.right = node
        node.left = temp

        node._get_height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        left_node._get_height = max(self._get_height(left_node.left), self._get_height(left_node.right)) + 1

        return left_node

    def _search(self, node, value):
        if not node or node.value == value:
            return node

        if node.value < value:
            return self._search(node.right, value)

        return self._search(node.left, value)
