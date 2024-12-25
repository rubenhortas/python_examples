#!/usr/bin/env python3

def get_sums(numbers: list, target: int) -> list:
    """
    Find all combinations of numbers in a list that add up to the target value.
    If there are no combinations return an empty list.
    :param numbers: [1, 5, 3, 2]
    :param target: 6
    :return: [[1, 5], [1, 3, 2]]
    """

    def get_sum(combination: list, start: int, target: int) -> list | None:
        if target == 0:  # Solution found
            solutions.append(combination[:])  # Shallow copy
            return

        if target < 0 or start == lenght:  # It has not solution
            return

        for i in range(start, lenght):
            if i > start and numbers[i] == numbers[i - 1]:
                continue

            combination.append(numbers[i])
            get_sum(combination, i + 1, target - numbers[i])
            combination.pop()  # Backtracking

    solutions = []
    lenght = len(numbers)

    numbers.sort()
    get_sum([], 0, target)

    return solutions
