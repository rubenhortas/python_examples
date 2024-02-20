#!/usr/bin/env python3

if __name__ == '__main__':
    for i in range(5):
        print(f"{i} ", end='')
    # return: 0 1 2 3 4

    print()

    for i in reversed(range(5)):
        print(f"{i} ", end='')
    # return: 4 3 2 1 0

    print()

    for i in range(10, 0, -2):  # (start, stop, step)
        print(f"{i} ", end='')
    # return: 10 8 6 4 2
