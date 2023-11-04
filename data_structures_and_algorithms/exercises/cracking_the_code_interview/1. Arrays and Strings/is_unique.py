#!/usr/bin/env python3

# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

UNIQUE_STRING = 'abcdefghij'
NOT_UNIQUE_STRING = "abcdefabcd"


def _is_unique(string: str) -> bool:
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


def _is_Unique_without_structures(string: str) -> bool:
    # Time complexity: O(n^2)
    # Auxiliary space: O(1)

    # What if you cannot use additional data structures?
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False

    return True


if __name__ == '__main__':
    print(_is_unique(UNIQUE_STRING))  # True
    print(_is_unique(NOT_UNIQUE_STRING))  # False

    print(_is_Unique_without_structures(UNIQUE_STRING))  # True
    print(_is_Unique_without_structures(NOT_UNIQUE_STRING))  # False
