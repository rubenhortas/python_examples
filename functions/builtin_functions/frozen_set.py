#!/usr/bin/env python3

"""
The frozenset() is an inbuilt function in Python which takes an iterable object as input and makes it immutable.
frozenset() simply freezes the iterable objects and makes them unchangeable.
If you want to change the frozenset an exception will raise.
"""

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    frozen_numbers = frozenset(numbers)

    try:
        # noinspection PyUnresolvedReferences
        frozen_numbers[1] = 0
    except TypeError as ex:
        print(ex)
        # return: 'frozenset' object does not support item assignment
