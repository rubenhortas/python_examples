#!/usr/bin/env python3

"""
Since python 3.8, the walrus operator ( := ) gives a new syntax for assigning variables in the middle of expressions.
A traditional assignment doesn't return the value, an assignment expression, with :=, it does.

Walrus operator use cases:
* Repeated function calls can make your code slower than necessary.
* Repeated statements can make your code hard to maintain.
* Repeated calls that exhaust iterators can make your code overly complex.
"""

import random

NUMBERS = [2, 8, 0, 1, 1, 9, 7, 7]


# noinspection PyShadowingNames
def _get_numbers_descriptive_statistics(numbers: list) -> None:
    # The variables num_length and num_sum are only used to optimize the calculations inside the dictionary.
    # By using the walrus operator, this role can be made more clear:

    # Without the walrus operator we would need the following two lines:
    # num_length = len(numbers)
    # num_sum = sum(numbers)

    description = {
        # Without the walrus operator we would need the following two lines:
        # "length": numbers_length,
        # "sum": numbers_sum,

        "length": (numbers_length := len(numbers)),
        "sum": (numbers_sum := sum(numbers)),
        "mean": numbers_sum / numbers_length,
    }

    print(description)  # {'length': 8, 'sum': 35, 'mean': 4.375}


# noinspection PyShadowingNames
def _do_calculations(numbers: list) -> None:
    # Using filter
    # results = filter(lambda value: value > 0, (_do_expensive_operation(num) for num in numbers))

    # Using a double list comprehension
    # results = [value for num in numbers for value in [_do_expensive_operation(num)] if value > 0]

    # Walrus operator improves code’s readability
    results = [value for num in numbers if (value := _do_expensive_operation(num)) > 0]

    print(results)  # return: [3, 4, 2, 2]


def _do_expensive_operation(n: int) -> int:
    return n - 5  # Yep, not very expensive...


# Assignment expressions can often be used to simplify while loops
def _print_random_number() -> None:
    while (number := random.randint(1, 100)) < 50:
        pass

    print(number)


if __name__ == '__main__':
    _get_numbers_descriptive_statistics(NUMBERS)
    _do_calculations(NUMBERS)
    _print_random_number()
