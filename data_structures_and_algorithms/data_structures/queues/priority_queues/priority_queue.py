"""
A Priority Queue is an abstract data structure where each element has an associated priority.
Elements with higher priority (or lower priority values in a min-heap) are dequeued before
elements with lower priority.

When to use:
- Event-driven simulations (processing events in chronological order).
- Graph algorithms (e.g., Dijkstra's shortest path, A* search).
- CPU task scheduling / Resource allocation based on task urgency.
- Streaming Top-K element tracking without sorting full datasets.
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import TypeVar

T = TypeVar("T")


@dataclass(order=True, slots=True)
class _PriorityItem[T]:
    """Internal wrapper to maintain heap ordering and break priority ties safely."""

    priority: int
    sequence: int = field(compare=True)
    item: T = field(compare=False)


class PriorityQueue[T]:
    """Thread-unsafe, high-performance Min-Priority Queue backed by a binary heap."""

    __slots__ = ("_counter", "_heap")

    def __init__(self) -> None:
        self._heap: list[_PriorityItem[T]] = []
        self._counter: int = 0

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        """Return True if the priority queue contains no elements."""
        return len(self._heap) == 0

    def push(self, item: T, priority: int) -> None:
        """
        Push an item into the queue with a given priority.

        Time Complexity: O(log N)
        """
        entry = _PriorityItem(priority=priority, sequence=self._counter, item=item)
        heapq.heappush(self._heap, entry)
        self._counter += 1

    def pop(self) -> T:
        """
        Pop and return the item with the lowest priority value.

        Raises:
            IndexError: If the queue is empty.

        Time Complexity: O(log N)
        """
        if not self._heap:
            raise IndexError("pop from an empty priority queue")  # noqa: TRY003

        entry = heapq.heappop(self._heap)
        return entry.item

    def peek(self) -> T:
        """
        Return the item with the lowest priority value without removing it.

        Raises:
            IndexError: If the queue is empty.

        Time Complexity: O(1)
        """
        if not self._heap:
            raise IndexError("peek from an empty priority queue")  # noqa: TRY003

        return self._heap[0].item
