#!/usr/bin/env python3

"""
Write output in the same line.
We can overwrite the text on the same line using the carriage return '\r'.
"""

import time

if __name__ == '__main__':
    print('Loading...')

    for i in range(10):
        print(f"\rProgress {i * 10}", end='')
        time.sleep(1)

    print('Done')
