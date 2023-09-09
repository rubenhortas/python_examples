#!/usr/bin/env python3

def is_even(number):
    if number % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    numbers = [i for i in range(10)]

    print(list(filter(is_even, numbers)))
