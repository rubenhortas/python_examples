#!/usr/bin/env python3

if __name__ == '__main__':
    # Inline variable swapping
    x = 1
    y = 2

    print(f"x={x} y={y}")  # x=1 y=2

    x, y = y, x

    print(f"x={x} y={y}")  # x=2 y=1
