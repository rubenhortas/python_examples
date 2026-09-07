#!/usr/bin/env python3

import unittest

from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    # Immutable default class attributes for Basedpyright + Ruff (RUF012) compliance
    pq: PriorityQueue[str]

    def setUp(self) -> None:
        self.pq = PriorityQueue[str]()

    def test_push_and_pop_ordering(self) -> None:
        self.pq.push("task_low", priority=10)
        self.pq.push("task_high", priority=1)
        self.pq.push("task_medium", priority=5)

        self.assertEqual(self.pq.pop(), "task_high")
        self.assertEqual(self.pq.pop(), "task_medium")
        self.assertEqual(self.pq.pop(), "task_low")

    def test_tie_breaking_fifo(self) -> None:
        """Equal priority items should be returned in FIFO order of insertion."""
        self.pq.push("first_inserted", priority=2)
        self.pq.push("second_inserted", priority=2)

        self.assertEqual(self.pq.pop(), "first_inserted")
        self.assertEqual(self.pq.pop(), "second_inserted")

    def test_peek_does_not_mutate(self) -> None:
        self.pq.push("critical", priority=0)

        self.assertEqual(self.pq.peek(), "critical")
        self.assertEqual(len(self.pq), 1)
        self.assertFalse(self.pq.is_empty())

    def test_pop_empty_queue_raises(self) -> None:
        with self.assertRaises(IndexError):
            self.pq.pop()

    def test_peek_empty_queue_raises(self) -> None:
        with self.assertRaises(IndexError):
            self.pq.peek()


if __name__ == "__main__":
    unittest.main()
