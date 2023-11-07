#!/usr/bin/env python3
from collections import Counter

# Given two strings, write a method to decide if one is a permutation of the other.

# We will assume the following:
#   * Permutation is case-sensitive
#   * Whitespaces are significant
#   * ASCII encoding

STR1 = 'check permutations'
STR2 = 'permutations check'


def _is_permutation_sorting(str1: str, str2: str) -> bool:
    # Time complexity: O(nlog(n))
    # Auxiliary space: O(1)
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)


def _is_permutation(str1: str, str2: str) -> bool:
    # Time complexity: O(n)
    # Auxiliary space: O(1)
    counter = [0] * 128

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        position = ord(str1[i])
        counter[position] = counter[position] + 1

    for i in range(len(str2)):
        position = ord(str2[i])
        counter[position] = counter[position] - 1

        if counter[position] < 0:
            return False

    return True


def _is_permutation_count(str1: str, str2: str) -> bool:
    # Pythonic way using Counter
    return Counter(str1) == Counter(str2)


if __name__ == '__main__':
    print(_is_permutation(STR1, STR2))  # True
    print(_is_permutation_sorting(STR1, STR2))  # True
    print(_is_permutation_count(STR1, STR2))  # True
