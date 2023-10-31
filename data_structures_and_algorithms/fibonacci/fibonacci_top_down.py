#!/usr/bin/env python3

"""
Top-down dynamic programming or memoization.

This approach consists of dividing the problem case N into subproblems.
"""


def fibonacci(n: int) -> int:
    values = [-1] * (n + 1)

    return _fibonacci(n, values)


def _fibonacci(n: int, values: list) -> int:
    if n <= 1:
        values[n] = n  # or return n

    if values[n] == -1:
        values[n] = _fibonacci(n - 1, values) + _fibonacci(n - 2, values)

    return values[n]
