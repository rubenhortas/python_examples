#!/usr/bin/env python3

import sys

"""
Operators:
a & b  AND
a | b  OR
a ^ b  XOR
~a     NOT
a << n Left shift
a >> n Right shift

Compound operators:
a &= b ->	a = a & b
a |= b -> a = a | b
a ^= b -> a = a ^ b
a <<= n -> a = a << n
a >>= n -> a = a >> n
"""


# noinspection PyShadowingNames
def get_bit(number: int, index: int) -> int:
    """
    Reads the value of a bit on a given position.
    The mask will suppress all bits except for the one that we are interested in.
    It will result in either zero or a power of two with an exponent equal to the bit index.
    :param number: 01000001
    :param index: 1
    :return: 1000001  # 64
    """
    return number & (1 << index)


def get_bit_value(number: int, index: int) -> int:
    """
    Shifts the bit int the given index to the right and then check the least significant bit
    If bit is 1 returns 1. If the bit is 0 returns 0.
    :param number: 01000001
    :param index: 6
    :return: 1
    """
    return (number >> index) & 1


# noinspection PyShadowingNames
def set_bit(number: int, index: int) -> int:
    """
    Sets the number of a bit on a given position to 1.
    :param number: 01000001
    :param index: 7
    :return: 11000001
    """
    return number | (1 << index)


# noinspection PyShadowingNames
def clear_bit(number: int, index: int) -> int:
    """
    Set the number of a bit on a given position to 0.
    :param number: 01000001
    :param index: 0
    :return: 01000000
    """
    return number & ~(1 << index)


# noinspection PyShadowingNames
def toggle_bit(number: int, index: int) -> int:
    """
    Toggle the number of a bit on a given position.
    :param number: 01000001
    :param index: 0
    :return: 01000001
    """
    return number ^ (1 << index)


if __name__ == '__main__':
    print(f'Byteorder: {sys.byteorder}')  # little/big endian
    # Byteorder: little

    number = 0b01000001  # ord('A') = 65
    print(f'{number:08b}')  # 01000001

    most_significant_bit = get_bit(number, 7)
    print(f'Most Significant Bit: {most_significant_bit:b} ({most_significant_bit})')

    second_most_significant_bit = get_bit(number, 6)
    print(f'Second Most Significant Bit: {second_most_significant_bit:b} ({second_most_significant_bit})')

    most_significant_bit_value = get_bit_value(number, 7)
    print(f'Most significant bit value: {most_significant_bit_value}')

    least_significant_bit_value = get_bit_value(number, 0)
    print(f'Least significant bit value: {least_significant_bit_value}')

    number = clear_bit(number, 0)
    print(f'Least significant bit cleared: {number:08b}')
    # 01000001
    # Least significant bit cleared: 01000000

    number = set_bit(number, 0)
    print(f'Least significant bit set: {number:08b}')
    # 01000001
    # Least significant bit set: 01000001

    number = toggle_bit(number, 0)
    print(f'Least significant bit toggled: {number:08b}')
    # 01000001
    # Least significant bit toggled: 01000000
