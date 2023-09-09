#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    queue = deque()

    # Adding elements as they arrive
    queue.append("First")
    queue.appendleft("Second")
    queue.appendleft("Third")

    print(queue)

    for i in list(queue):
        queue.popleft()  # Since queues are LIFO, the last element who got into the stack should be the first to get out
        print(queue)
