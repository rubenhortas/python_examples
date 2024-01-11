#!/usr/bin/env python3

def fibonacci(n: int) -> int:
    # Time complexity: O(2^n)
    # Auxiliary space: O(n)

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
