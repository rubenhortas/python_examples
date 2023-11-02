#!/usr/bin/env python3

"""
Filtering iterables with filter()
filter() return a new iterable with those items that meet the condition.
"""


def _is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    numbers = [i for i in range(10)]

    print(list(filter(_is_even, numbers)))
    # return: [0, 2, 4, 6, 8]
