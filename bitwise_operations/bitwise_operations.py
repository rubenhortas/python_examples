#!/usr/bin/env python3

import sys


# Operators:
# a & b  AND
# a | b  OR
# a ^ b  XOR
# ~a     NOT
# a << n Left shift
# a >> n Right shift

# Compound operators:
# a &= b ->	a = a & b
# a |= b -> a = a | b
# a ^= b -> a = a ^ b
# a <<= n -> a = a << n
# a >>= n -> a = a >> n

# Read the value of a bit on a given position
# noinspection PyShadowingNames
def get_bit(number, index):
    return number & (1 << index)


# Shift the bit int the given index to the right and then check the least significant bit
# If the least significant bit is 1 returns 1
# If the least significant bit is 0 returns 0
def get_bit_value(number, index):
    return (number >> index) & 1


# Set the number of a bit on a given position to 1
# noinspection PyShadowingNames
def set_bit(number, index):
    return number | (1 << index)


# Set the number of a bit on a given position to 0
# noinspection PyShadowingNames
def clear_bit(number, index):
    return number & ~(1 << index)


# Toggle the number of a bit on a given position
# noinspection PyShadowingNames
def toggle_bit(number, index):
    return number ^ (1 << index)


if __name__ == '__main__':
    print(f'Byteorder: {sys.byteorder}')  # little/big endian
    # Byteorder: little

    number = 0b01000001  # ord('A') = 65
    print(f'{number:08b}')
    # 01000001

    most_significant_bit = get_bit(number, 7)
    print(f'Most Significant Bit: {most_significant_bit:b} ({most_significant_bit})')
    # 01000001
    # Most Significant Bit: 0 (0)

    second_most_significant_bit = get_bit(number, 6)
    print(f'Second Most Significant Bit: {second_most_significant_bit:b} ({second_most_significant_bit})')
    # 01000001
    # Second Most Significant Bit: 1000000 (64)

    most_significant_bit_value = get_bit_value(number, 7)
    print(f'Most significant bit value: {most_significant_bit_value}')
    # 01000001
    # Most significant bit value: 0

    least_significant_bit_value = get_bit_value(number, 0)
    print(f'Least significant bit value: {least_significant_bit_value}')
    # 01000001
    # Least significant bit value: 1

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
