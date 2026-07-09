import unittest

from data_structures_and_algorithms.data_structures.heap.max_heap import MaxHeap
from data_structures_and_algorithms.data_structures.heap.min_heap import MinHeap


class Test(unittest.TestCase):
    def test_min_heap(self) -> None:
        min_heap: MinHeap = MinHeap(10)
        min_heap.insert(10)
        min_heap.insert(5)
        min_heap.insert(15)
        min_heap.insert(4)
        min_heap_expected_min = 4
        min_heap_expected_second_min = 5

        self.assertEqual(min_heap_expected_min, min_heap.get_min())
        min_heap.extract_min()
        self.assertEqual(min_heap_expected_second_min, min_heap.get_min())

    def test_max_heap(self) -> None:
        max_heap = MaxHeap(10)
        max_heap.insert(10)
        max_heap.insert(5)
        max_heap.insert(15)
        max_heap.insert(4)
        max_heap_expected_max = 15
        max_heap_expected_second_max = 10

        self.assertEqual(max_heap_expected_max, max_heap.get_max())
        max_heap.extract_max()
        self.assertEqual(max_heap_expected_second_max, max_heap.get_max())
