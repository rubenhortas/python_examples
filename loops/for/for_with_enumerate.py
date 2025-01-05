#!/usr/bin/env python3

NUMBERS = ['One', 'Two', 'Three', 'Four']

if __name__ == '__main__':
    # enumerate() function is used with the for loop to iterate over an iterable while also keeping track of index of each item.
    for i, j in enumerate(NUMBERS):
        print(i, j)
    # return:
    # 0 One
    # 1 Two
    # 2 Three
    # 3 Four
