"""
A min heap is a complete binary tree where the value of each node is less than or equal to the values of its children.
"""

from binary_heap import BinaryHeap


class MinHeap(BinaryHeap):
    def _heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        smallest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def extract_min(self):
        return self._extract_root()

    def get_min(self):
        return self._get_root()
