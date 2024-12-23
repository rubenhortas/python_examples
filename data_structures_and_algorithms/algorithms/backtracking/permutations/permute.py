#!/usr/bin/env python3

def _swap(s: str, index: int, position: int) -> str:
    if position == index:
        return s

    s = list(s)
    s[index], s[position] = s[position], s[index]

    return ''.join(s)


def get_permutations(string: str) -> list:
    """
    Gets all the permutations of a given string.
    :param string: 'ABC'
    :return: ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']
    """

    def get_permutation(s: str, index: int) -> list | None:
        if index == length - 1:
            solutions.append(s)
            return

        for i in range(index, length):
            s = _swap(s, index, i)

            get_permutation(s, index + 1)

            s = _swap(s, index, i)  # Backtrack

    if not string:
        return []

    solutions = []
    length = len(string)

    get_permutation(string, 0)

    return solutions
