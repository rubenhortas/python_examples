import unittest

from min_heap import MinHeap
from max_heap import MaxHeap


class Test(unittest.TestCase):
    def setUp(self):
        self.min_heap = MinHeap(10)
        self.min_heap.insert(10)
        self.min_heap.insert(5)
        self.min_heap.insert(15)
        self.min_heap.insert(4)
        self.min_heap_expected_min = 4
        self.min_heap_expected_second_min = 5
        
        self.max_heap = MaxHeap(10)
        self.max_heap.insert(10)
        self.max_heap.insert(5)
        self.max_heap.insert(15)
        self.max_heap.insert(4)
        self.max_heap_expected_max = 15
        self.max_heap_expected_second_max = 10

    def test_min_heap(self):
        self.assertEqual(self.min_heap_expected_min, self.min_heap.get_min())
        self.assertEqual(self.min_heap_expected_min, self.min_heap.extract_min())
        self.assertEqual(self.min_heap_expected_second_min, self.min_heap.get_min())
        
    def test_max_heap(self):
        self.assertEqual(self.max_heap_expected_max, self.max_heap.get_max())
        self.assertEqual(self.max_heap_expected_max, self.max_heap.extract_max())
        self.assertEqual(self.max_heap_expected_second_max, self.max_heap.get_max())
