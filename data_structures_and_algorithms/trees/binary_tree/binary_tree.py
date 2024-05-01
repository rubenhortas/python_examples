from queue import Queue

from binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_node: BinaryTreeNode):
        """
        Insertion in level order.

        Time complexity: O(n)
        Auxiliary space: O(n)
        """
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

    def get_inorder_traversal(self) -> list:
        """
        1. Traverse the left subtree
        2. Visit the root
        3. Traverse the right subtree

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_inorder(node: BinaryTreeNode, values: list) -> None:
            if node:
                traverse_inorder(node.left, values)
                values.append(str(node))
                traverse_inorder(node.right, values)

        values = []
        traverse_inorder(self.root, values)
        return values

    def get_preorder_traversal(self) -> list:
        """
        1. Visit the root
        2. Traverse the left subtree
        3. Traverse the right subtree

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_preorder(node: BinaryTreeNode, values: list) -> None:
            if node:
                values.append(str(node))
                traverse_preorder(node.left, values)
                traverse_preorder(node.right, values)

        values = []
        traverse_preorder(self.root, values)
        return values

    def get_postorder_traversal(self) -> list:
        """
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_postorder(node: BinaryTreeNode, values: list) -> None:
            if node:
                traverse_postorder(node.left, values)
                traverse_postorder(node.right, values)
                values.append(str(node))

        values = []
        traverse_postorder(self.root, values)
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
