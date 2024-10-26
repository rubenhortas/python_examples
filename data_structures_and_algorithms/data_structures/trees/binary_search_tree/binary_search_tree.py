"""
Binary search tree (BST) is a special type of binary tree in which the left child of a node has a value less
than the node's value and the right child has a value greater than the node's value.
"""

from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        def insert_node(node: Node) -> None:
            if value < node.value:
                if not node.left:
                    node.left = Node(value)
                else:
                    insert_node(node.left)
            elif value == node.value:
                node.count += 1
            else:
                if not node.right:
                    node.right = Node(value)
                else:
                    insert_node(node.right)

        if not self.root:
            self.root = Node(value)
        else:
            insert_node(self.root)

    def get_inorder_traversal(self) -> list:
        def traverse_inorder(node: Node) -> None:
            if node:
                traverse_inorder(node.left)
                values.append(str(node))
                traverse_inorder(node.right)

        values = []
        traverse_inorder(self.root)
        return values
