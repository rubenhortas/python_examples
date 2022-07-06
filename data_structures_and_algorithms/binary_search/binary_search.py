#!/usr/bin/env python3

# Write a program to find the position of a given number in a list of numbers arranged in **decreasing** order.
# Minimize the number of times we access elements from the list.

# This is my pythonic way to implement a binary search
# Instead passing as arguments the whole list, the number sought, the min position and the max position
# I decided to pass only the half of the list that interests and the number sought
# Which turned out to be slightly more memory efficient

# Time Complexity: O(log n)
# Auxiliary Space: O(1)
def locate_position(lst, number):
    if len(lst) > 0:
        pos = len(lst) // 2
        mid = lst[pos]

        if number > mid:
            return locate_position(lst[:pos], number)
        elif number < mid:
            return pos + locate_position(lst[pos:], number)
        else:
            if _is_first_appearance(lst, number, pos):
                return pos
            else:
                return locate_position(lst[:pos], number)
    else:
        return -1


def _is_first_appearance(lst, number, pos):
    prev_pos = pos - 1
    return not (prev_pos > 0 and lst[prev_pos] == number)
