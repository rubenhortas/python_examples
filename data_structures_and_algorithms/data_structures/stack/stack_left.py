from collections import deque


class StackLeft:
    def __init__(self) -> None:
        self.queue = deque()

    def __str__(self) -> str:
        return str(list(self.queue))

    def append(self, item: str) -> None:
        # Adding elements as they arrive
        self.queue.appendleft(item)  # Add to the left side

    def pop(self) -> None:
        # Since queues are LIFO, the last element who got into the stack should be the first to get out
        self.queue.popleft()
