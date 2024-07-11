#!/usr/bin/env python3

LIST0 = [0, 0, 0, 0, 0, 0, 0, 0]
LIST2 = [0, 0, 0, 0, 0, 0, 0, 1]
ALPHAS = ['0', '0', '0', 'a', '0', '0']
DIGITS = ['0', '0', '0', '0', '0', '0']

if __name__ == '__main__':
    # any returns True if bool(x) is True for any x in the iterable.
    print(any(LIST0))
    # return: False

    print(any(LIST2))
    # return: True

    print(any(item.isalpha() for item in ALPHAS))
    # return: True

    print(any(item.isalpha() for item in DIGITS))
    # return: False
