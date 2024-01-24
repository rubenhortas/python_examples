"""
A good example of a Python program that can put the CPU at 100% usage involves creating a CPU-intensive task
and then distributing this task across all CPU cores using the multiprocessing module.
"""

import math
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def _intensive_task(n: int) -> int:
    # CPU-intensive task
    return sum([math.sqrt(i) for i in range(1, n)])


if __name__ == '__main__':
    print('Starting task...')

    with ProcessPoolExecutor(multiprocessing.cpu_count()) as exe:
        results = list(exe.map(_intensive_task, range(1, 50000)))  # distributing this task across all CPU cores

    print('Done.')
