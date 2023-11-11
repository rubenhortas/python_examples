#!/usr/bin/env python3
from collections import Counter


# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique(string: str) -> bool:
    # Time complexity: O(n)
    # Auxiliary space: O(1)

    # Let's assume that is an ASCII string.
    # ASCII has just 128 code points, of which only 95 are printable characters.
    # UTF-8 is capable of encoding all 1,112,064[a] valid Unicode code points.
    # If it were a UTF-8 string, we would need to use more memory.
    chars = [False] * 128

    for i in range(len(string)):
        if chars[ord(string[i])]:
            return False

        chars[ord(string[i])] = True

    return True


# What if you cannot use additional data structures?
def is_unique_without_structures(string: str) -> bool:
    # Time complexity: O(n^2)
    # Auxiliary space: O(1)

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False

    return True


def is_unique_set(string: str) -> bool:
    # Pythonic way using set
    return len(string) == len(set(string))


def is_unique_counter(string: str) -> bool:
    # Pythonic way using Counter
    counter = Counter(string)

    for char in counter:
        if counter[char] > 1:
            return False

    return True


def is_unique_count(string: str) -> bool:
    # Pythonic way using count
    for char in string:
        if string.count(char) > 1:
            return False

    return True
