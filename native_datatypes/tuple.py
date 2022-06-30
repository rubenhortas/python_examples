#!/usr/bin/env python3

# A tuple is an immutable list. A tuple can not be changed in any way once it is created.
# Tuples doesn't have append(), extend(), insert(), remove(), or pop()
# Tuples are faster than lists
# With tuples you can protect data from read/write

EMPTY = ()
ITEMS = ("a", "b", "c")

if __name__ == '__main__':
    # Tuples in a boolean context
    # An empty tuple is False otherwise is True
    if ITEMS:
        print(f"{ITEMS} has items")

    if not EMPTY:
        print(f"{EMPTY} is empty")
