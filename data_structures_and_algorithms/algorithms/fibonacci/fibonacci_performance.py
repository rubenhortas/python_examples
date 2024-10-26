#!/usr/bin/env python3

from data_structures_and_algorithms.algorithms.fibonacci import fibonacci_top_down, fibonacci_bottom_up, \
    fibonacci_recursive
from performance.execution_time import get_execution_time

N = 100


@get_execution_time
def _fib_recursive() -> None:
    fibonacci_recursive.fibonacci(N)


@get_execution_time
def _fibonacci_top_down() -> None:
    fibonacci_top_down.fibonacci(N)


@get_execution_time
def _fibonacci_bottom_up() -> None:
    fibonacci_bottom_up.fibonacci(N)


if __name__ == '__main__':
    results = {
        'Fibonacci recursive O(2^n), O(n)': _fib_recursive(),
        'Fibonacci top down O(n), O(n)': _fibonacci_top_down(),
        'Fibonacci bottom up O(n), O(1)': _fibonacci_bottom_up()
    }

    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=False)

    for result in sorted_results:
        print(f"* {result[0]}: {result[1]:.5f}")

    # Results (sorted from faster to slower):
    #    * Fibonacci bottom up O(n), O(1)
    #    * Fibonacci top down O(n), O(n)
    #    * Fibonacci recursive O(2^n), O(n)
