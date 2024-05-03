from collections import deque
from queue import Queue

from binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_value: str) -> None:
        """
        Insertion in level order traversal.

        Time complexity: O(n)
        Auxiliary space: O(n)
        """
        new_node = BinaryTreeNode(new_value)

        if self.root:
            queue = Queue()
            queue.put(self.root)

            while not queue.empty():
                node = queue.get()

                if node:
                    if node.left:
                        queue.put(node.left)
                    else:
                        node.left = new_node
                        break

                    if node.right:
                        queue.put(node.right)
                    else:
                        node.right = new_node
                        break
        else:
            self.root = new_node

    def delete(self, value: str) -> None:
        """
        Deletion of a node using level order traversal.
        The deleted node is replaced by the bottom-most and rightmost node.

        Time complexity: O(n)
        Auxiliary Space: O(n)
        """

        def delete_node(node_to_delete: BinaryTreeNode) -> None:
            queue = Queue()
            queue.put(self.root)

            while not queue.empty():
                node = queue.get()

                if node.left == node_to_delete:
                    node.left = None
                    return
                else:
                    queue.put(node.left)

                if node.right == node_to_delete:
                    node.right = None
                    return
                else:
                    queue.put(node.right)

        if self.root:
            queue = Queue()
            queue.put(self.root)
            deepest_rightmost_node = None
            node_to_delete = None

            while not queue.empty():
                node = queue.get()

                if node:
                    deepest_rightmost_node = node

                    if str(node.value) == value:
                        node_to_delete = node

                    queue.put(node.left)
                    queue.put(node.right)

            if node_to_delete:
                if node_to_delete != deepest_rightmost_node:
                    node_to_delete.value = deepest_rightmost_node.value

                delete_node(deepest_rightmost_node)

    def get_height(self) -> int:
        def get_node_height(node: BinaryTreeNode) -> int:
            if not node:
                return 0

            left_height = get_node_height(node.left)
            right_height = get_node_height(node.right)

            return 1 + (left_height if left_height > right_height else right_height)

        return get_node_height(self.root)

    def get_inorder_traversal(self) -> list:
        """
        1. Traverse the left subtree
        2. Visit the root
        3. Traverse the right subtree

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_inorder(node: BinaryTreeNode) -> None:
            if node:
                traverse_inorder(node.left)
                values.append(str(node))
                traverse_inorder(node.right)

        values = []
        traverse_inorder(self.root)
        return values

    def get_preorder_traversal(self) -> list:
        """
        1. Visit the root
        2. Traverse the left subtree
        3. Traverse the right subtree

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_preorder(node: BinaryTreeNode) -> None:
            if node:
                values.append(str(node))
                traverse_preorder(node.left)
                traverse_preorder(node.right)

        values = []
        traverse_preorder(self.root)
        return values

    def get_postorder_traversal(self) -> list:
        """
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_postorder(node: BinaryTreeNode) -> None:
            if node:
                traverse_postorder(node.left)
                traverse_postorder(node.right)
                values.append(str(node))

        values = []
        traverse_postorder(self.root)
        return values

    def get_level_order_traversal(self) -> list:
        """
        Level order tree traversal algorithm is a breadth-first tree traversal algorithm.
        It means that while traversing a tree, we first traverse all the elements at the current level before moving to the next level.

        Time complexity: O(n)
        Auxiliary space: O(1)
        """
        values = []

        if self.root:
            queue = Queue()
            queue.put(self.root)

            while not queue.empty():
                node = queue.get()

                if node:
                    values.append(str(node))
                    queue.put(node.left)
                    queue.put(node.right)

        return values

    def get_lot_spiral(self) -> list:
        """
        Level order traversal in spiral form.

        Time complexity: O(n)
        Auxiliary space: O(n)
        """

        def get_level(node: BinaryTreeNode, level: int, left_to_right: bool) -> None:
            if node:
                if level == 1:
                    values.append(node.value)
                else:
                    if left_to_right:
                        get_level(node.left, level - 1, left_to_right)
                        get_level(node.right, level - 1, left_to_right)
                    else:
                        get_level(node.right, level - 1, left_to_right)
                        get_level(node.left, level - 1, left_to_right)

        values = []

        if self.root:
            height = self.get_height()
            left_to_right = False

            for i in range(1, height + 1):
                get_level(self.root, i, left_to_right)
                left_to_right = not left_to_right

        return values

    def get_lot_spiral_stacks(self) -> list:
        values = []

        if self.root:
            q1 = deque()
            q2 = deque()

            q1.appendleft(self.root)

            while q1 or q2:
                while q1:
                    node = q1.popleft()

                    if node:
                        values.append(node.value)

                        q2.appendleft(node.right)
                        q2.appendleft(node.left)

                while q2:
                    node = q2.popleft()

                    if node:
                        values.append(node.value)

                        q1.appendleft(node.left)
                        q1.appendleft(node.right)

        return values
