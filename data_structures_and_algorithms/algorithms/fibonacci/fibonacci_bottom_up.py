"""
Bottom-up dynamic programming.

This approach consists of build the solution for one case off the previous case (or multiple previous cases).
"""


def fibonacci(n: int) -> int:
    # Time complexity: O(n)
    # Auxiliary space: O(1)

    if n <= 1:
        return n

    # We don't need to store the computed values into an array.
    # We only need the last two values.
    result = 0
    nm2 = 0  # n minus 2, n - 2
    nm1 = 1  # n minus 1, n - 1

    for _ in range(2, n + 1):
        result = nm1 + nm2

        nm2 = nm1
        nm1 = result

    return result
