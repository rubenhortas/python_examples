#!/usr/bin/env python3

# Time complexity: O(2^n)
# Auxiliary space: O(n)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
