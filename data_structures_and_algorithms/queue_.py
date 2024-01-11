#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    queue = deque()

    # Adding elements as they arrive
    queue.append('First')
    queue.append('Second')
    queue.append('Third')

    print(queue)
    # return: deque(['First', 'Second', 'Third'])

    for i in list(queue):
        queue.popleft()  # Since queues are FIFO, the first element who got into the queue should be the first to get out
        print(queue)

    # return:
    #   deque(['Second', 'Third'])
    #   deque(['Third'])
    #   deque([])
