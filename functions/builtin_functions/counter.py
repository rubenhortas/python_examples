#!/usr/bin/env python3

from collections import Counter

# noinspection SpellCheckingInspection
LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore"

if __name__ == '__main__':
    # You can use Counter from the collections' library to get a dictionary with counts of all the unique elements in a list
    print(f"Lorem ipsum counter: {Counter(LOREM_IPSUM)}")
