def get_position(lst: list, number: int) -> int:
    """
    Finds the position of a given number in a list of numbers arranged in decreasing order.
    :param lst: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    :param number: 4
    :return: 5
    """
    return _binary_search(lst, number, 0, len(lst) - 1)


def _binary_search(lst: list, number: int, min_pos: int, max_pos: int) -> int:
    # Time complexity: O(log(n))
    # Auxiliary space: O(1)

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
