"""
A binary heap is a heap data structure that takes the form of a binary tree.
It's a fundamental data structure used in various algorithms like heap sort, priority queues, and graph algorithms.
"""


class BinaryHeap:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the heap
        self.size = 0  # Current number of elements in the heap
        self.heap = [0] * capacity  # Array to store the heap elements

    def insert(self, x):
        if self.size == self.capacity:
            return None

        self.heap[self.size] = x
        self.size += 1
        self._heapify_up(self.size - 1)

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left_child(i):
        return 2 * i + 1

    @staticmethod
    def _right_child(i):
        return 2 * i + 2

    def _heapify_up(self, i):
        """
        Moves an element up the tree if it's smaller than its parent.
        """
        raise Exception('Not implemented')

    def _heapify_down(self, i):
        """
        Moves an element down the tree to maintain the heap property.:
        """
        raise Exception('Not implemented')

    def _extract_root(self):
        """
        Removes and returns the minimum element (root) and heapifies down.
        """
        if self.size == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self._heapify_down(0)

        return root

    def _get_root(self):
        """
        Returns the minimum element without removing it.
        """
        if self.size == 0:
            return None

        return self.heap[0]
