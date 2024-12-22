#!/usr/bin/env python3

def get_sums(numbers: list, target: int) -> list:
    def get_sum(combination: list, index: int, target: int) -> list | None:
        if target == 0:  # Solution found
            solutions.append(combination[:])  # Shallow copy
            return

        if target < 0 or index == len(numbers):  # It has not solution
            return

        for i in range(index, len(numbers)):  # Backtracking
            if i > index and numbers[i] == numbers[i - 1]:
                continue

            combination.append(numbers[i])
            get_sum(combination, i + 1, target - numbers[i])
            combination.pop()

    solutions = []

    get_sum([], 0, target)

    return solutions


if __name__ == '__main__':
    print(get_sums([1, 5, 3, 2], 6))
