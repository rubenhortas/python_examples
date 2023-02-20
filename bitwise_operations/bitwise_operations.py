#!/usr/bin/env python3
import sys

# Operators:
# a & b  AND
# a | b  OR
# a ^ b  XOR
# ~a     NOT
# a << n Left shift
# a >> n Right shift
#
# Compound operators:
# a &= b ->	a = a & b
# a |= b -> a = a | b
# a ^= b -> a = a ^ b
# a <<= n -> a = a << n
# a >>= n -> a = a >> n


# Read the value of a bit on a given position
def get_bit(number, index):
    return number & (1 << index)


# Shift the bit int the given index to the right and then check the least significant bit
# If the least significant bit is 1 returns 1
# If the least significant bit is 0 returns 0
def get_bit_value(number, index):
    return (number >> index) & 1


# Set the number of a bit on a given position to 1
def set_bit(number, index):
    return number | (1 << index)


# Set the number of a bit on a given position to 0
def clear_bit(number, index):
    return number & ~(1 << index)


# Toggle the number of a bit on a given position
def toggle_bit(number, index):
    return number ^ (1 << index)


if __name__ == '__main__':
    print(f'Byteorder: {sys.byteorder}')  # little/big endian

    number = 0b01000001  # ord('A') = 65
    print(f'{number:08b}')

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

    number = set_bit(number, 0)
    print(f'Least significant bit set: {number:08b}')

    number = toggle_bit(number, 0)
    print(f'Least significant bit toggled: {number:08b}')
