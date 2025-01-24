"""
A max heap is a complete binary tree where the value of each node is greater than or equal to the values of its children.
"""

from binary_heap import BinaryHeap


class MaxHeap(BinaryHeap):
    def extract_max(self):
        return self._extract_root()

    def get_max(self):
        return self._get_root()

    def _heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)
