#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    numbers_range = range(100)
    numbers_list = [i for i in range(100)]

    # The range function returns a class that behaves like a list.
    # A range is much more memory efficient than a list.
    print(f"Size of range: {sys.getsizeof(numbers_range)} bytes")  # Size of range: 48 bytes
    print(f"Size of list: {sys.getsizeof(numbers_list)} bytes")  # Size of list: 920 bytes
