#!/usr/bin/env python3

if __name__ == '__main__':
    for i in range(10, 0, -1):  # (start, stop, step)
        print(f"{i} ", end='')
    # return: 10 9 8 7 6 5 4 3 2 1

    print()

    for i in reversed(range(10)):
        print(f"{i} ", end='')
    # return: 9 8 7 6 5 4 3 2 1 0
