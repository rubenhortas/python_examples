#!/usr/bin/env python3

LIST0 = [1, 1, 1, 1, 1, 1, 1, 1]
LIST2 = [1, 1, 1, 1, 1, 1, 1, 0]
ALPHAS = ['a', 'a', 'a', 'a', 'a', 'a']
DIGITS = ['a', 'a', 'a', 'a', 'a', '0']

if __name__ == '__main__':
    # all returns True if bool(x) is True for all values x in the iterable.
    print(all(LIST0))
    # return: True

    print(all(LIST2))
    # return: False

    print(all(item.isalpha() for item in ALPHAS))
    # return: True

    print(all(item.isalpha() for item in DIGITS))
    # return: False
