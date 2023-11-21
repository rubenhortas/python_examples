#!/usr/bin/env python3

# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

from collections import Counter


def is_permutation_of_palindrome_pythonic(string: str) -> bool:
    normalized_string = string.replace(' ', '').lower()
    counts = Counter(normalized_string)
    odd_chars = 0

    for c in counts:
        if counts[c] % 2 != 0:
            if len(normalized_string) % 2 == 0:
                return False
            else:
                odd_chars = odd_chars + 1

                if odd_chars > 1:
                    return False

    return True


def is_permutation_of_palindrome(string: str) -> bool:
    bit_vector = _create_bit_vector(string.replace(' ', '').lower())

    return bit_vector == 0 or _check_exactly_one_bit_set(bit_vector)


def _create_bit_vector(string: str) -> int:
    bit_vector = 0

    for c in string:
        bit_vector = _toggle(bit_vector, ord(c) - 1)

    return bit_vector


def _toggle(bit_vector: int, index: int) -> int:
    if index < 0:
        return bit_vector

    mask = 1 << index

    if (bit_vector & mask) == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask

    return bit_vector


def _check_exactly_one_bit_set(bit_vector: int) -> bool:
    return bit_vector & (bit_vector - 1) == 0
