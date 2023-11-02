#!/usr/bin/env python3

"""
Top-down dynamic programming or memoization.

This approach consists of dividing the problem case N into subproblems.
"""


# Time complexity: O(n)
# Auxiliary space: O(n)
def fibonacci(n: int) -> int:
    values = [-1] * (n + 1)

    # noinspection PyShadowingNames
    def _fibonacci(n: int) -> int:
        if n <= 1:
            values[n] = n  # or return n

        if values[n] == -1:
            values[n] = _fibonacci(n - 1) + _fibonacci(n - 2)

        return values[n]

    return _fibonacci(n)
