#!/usr/bin/env python3

# Write a program to find the position of a given number in a list of numbers arranged in decreasing order.
# Minimize the number of times we access elements from the list.

def locate_position(lst, number):
    if len(lst) > 0:
        pos = len(lst) // 2
        mid = lst[pos]

        if number > mid:
            return locate_position(lst[:pos], number)
        elif number < mid:
            return pos + locate_position(lst[pos:], number)
        else:
            return pos
    else:
        return -1
