#!/usr/bin/env python3

"""
The map() function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter.
"""

FRUITS = ['apple', 'banana', 'cherry']

if __name__ == '__main__':
    print('Map:')
    print(f"\tFruits: {FRUITS}")

    # map(function, iterables)
    print(f"\tLengths of fruits: {list(map(len, FRUITS))}")
    # return: Map:
    # 	        Fruits: ['apple', 'banana', 'cherry']
    # 	        Lengths of fruits: [5, 6, 6]
