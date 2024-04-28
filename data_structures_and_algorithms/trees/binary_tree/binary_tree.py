#!/usr/bin/env python3

from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def print_inorder_traversal(node: Node) -> None:
    """
    1. Traverse the left subtree
    2. Visit the root
    3. Traverse the right subtree

    Time complexity: O(n)
    Auxiliary space: O(1)
    """
    if node:
        print_inorder_traversal(node.left)
        print(node, end=' ')
        print_inorder_traversal(node.right)


def print_preorder_traversal(node: Node) -> None:
    """
    1. Visit the root
    2. Traverse the left subtree
    3. Traverse the right subtree

    Time complexity: O(n)
    Auxiliary space: O(1)
    """
    if node:
        print(node, end=' ')
        print_preorder_traversal(node.left)
        print_preorder_traversal(node.right)


def print_postorder_traversal(node: Node) -> None:
    """
    1. Traverse the left subtree
    2. Traverse the right subtree
    3. Visit the root

    Time complexity: O(n)
    Auxiliary space: O(1)
    """
    if node:
        print_postorder_traversal(node.left)
        print_postorder_traversal(node.right)
        print(node, end=' ')


def print_level_order_traversal(root: Node) -> None:
    """
    Level order tree traversal algorithm is a breadth-first tree traversal algorithm.
    It means that while traversing a tree, we first traverse all the elements at the current level before moving to the next level.

    Time complexity: O(n)
    Auxiliary space: O(1)
    """
    if root:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            node = queue.get()

            if node:
                print(node, end=' ')
                queue.put(node.left)
                queue.put(node.right)
