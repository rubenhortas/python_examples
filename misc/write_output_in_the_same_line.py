#!/usr/bin/env python3

"""
Write output in the same line.
"""

import time

if __name__ == '__main__':
    print('Loading...')

    for i in range(10):
        print(f"\rProgress {i * 10}", end='')
        time.sleep(1)

    print('Done')
