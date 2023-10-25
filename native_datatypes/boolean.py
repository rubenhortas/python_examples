#!/usr/bin/env python3

"""
Due to some legacy issues left over from Python 2, booleans can be treated as numbers.
True is 1; False is 0.
"""
if __name__ == '__main__':
    print(True + True)  # return:  2
    print(False + False)  # return: 0
    print(True - False)  # return: 1
    print(True * False)  # return: 0
