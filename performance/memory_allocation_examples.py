#!/usr/bin/env python3

import sys

from performance.memory_allocation import get_memory_allocation


# noinspection PyShadowingNames
@get_memory_allocation
def _create_list(size: int) -> list:
    lst = []

    for i in range(0, size - 1):
        lst.append(i)

    return lst


def _get_function_memory_allocation() -> None:
    size, peak = _create_list(100)
    print(f"Current memory size: {size} KiB, peak memory size: {peak} KiB")
    # return: Current memory size: 864 KiB, peak memory size: 896 KiB

    size, peak = _create_list(1000)
    print(f"Current memory size: {size} KiB, peak memory size: {peak} KiB")
    # return: Current memory size: 29576 KiB, peak memory size: 29608 KiB


def _get_object_memory_allocation() -> None:
    # The range function returns a class that behaves like a list.
    # A range is much more memory efficient than a list.
    numbers_range = range(100)
    numbers_list = [i for i in range(100)]

    print(f"Size of range: {sys.getsizeof(numbers_range)} bytes")
    # return: Size of range: 48 bytes

    print(f"Size of list: {sys.getsizeof(numbers_list)} bytes")
    # Size of list: 920 bytes


if __name__ == '__main__':
    _get_function_memory_allocation()
    _get_object_memory_allocation()
