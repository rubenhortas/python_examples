#!/usr/bin/env python3

from collections import Counter

# noinspection SpellCheckingInspection
LOREM_IPSUM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore'

if __name__ == '__main__':
    # You can use Counter from the collections library to get a dictionary with counts of all the unique elements in a list
    print(f'Lorem ipsum counter: {Counter(LOREM_IPSUM)}')
    # return: Lorem ipsum counter: Counter({' ': 14, 'i': 10, 'e': 9, 'o': 8, 't': 8, 'd': 7, 's': 6, 'r': 5, 'm': 5, 'u': 5, 'c': 4, 'n': 4, 'p': 3, 'l': 3, 'a': 3, ',': 2, 'L': 1, 'g': 1, 'b': 1})
