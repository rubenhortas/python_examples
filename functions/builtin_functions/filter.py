#!/usr/bin/env python3

"""
Filtering iterables with filter()
filter() return a new iterable with those items that meet the condition.
"""


def _is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    numbers = list(range(10))

    print(list(filter(_is_even, numbers)))
    # return: [0, 2, 4, 6, 8]
