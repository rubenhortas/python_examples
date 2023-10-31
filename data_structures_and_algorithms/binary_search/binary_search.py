#!/usr/bin/env python3

# Write a program to find the position of a given number in a list of numbers arranged in **decreasing** order.
# Minimize the number of times we access elements from the list.

# Time complexity: O(log(n))
# Auxiliary space: O(1)
def locate_position(lst: list, number: int) -> int:
    return _binary_search(lst, number, 0, len(lst) - 1)


def _binary_search(lst: list, number: int, min_pos: int, max_pos: int) -> int:
    if min_pos <= max_pos:
        mid_pos = (min_pos + max_pos) // 2

        if lst[mid_pos] > number:
            return _binary_search(lst, number, (mid_pos + 1), max_pos)
        elif lst[mid_pos] < number:
            return _binary_search(lst, number, min_pos, (mid_pos - 1))
        else:
            if _is_first_appearance(lst, number, mid_pos):
                return mid_pos
            else:
                return _binary_search(lst, number, min_pos, (mid_pos - 1))
    else:
        return -1


def _is_first_appearance(lst: list, number: int, pos: int) -> bool:
    prev_pos = pos - 1

    return not (prev_pos > 0 and lst[prev_pos] == number)
