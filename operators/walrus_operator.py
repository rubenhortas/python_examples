#!/usr/bin/env python3
import random


# Since python 3.8, the walrus operator ( := ) gives a new syntax for assigning variables in the middle of expressions.
# A traditional assignment doesn't return the value, an assignment expression, with :=, it does.
#
# Walrus operator use cases
# * Repeated function calls can make your code slower than necessary.
# * Repeated statements can make your code hard to maintain.
# * Repeated calls that exhaust iterators can make your code overly complex.

def get_numbers_descriptive_statistics(numbers):
    # The variables num_length and num_sum are only used to optimize the calculations inside the dictionary.
    # By using the walrus operator, this role can be made more clear:
    # num_length = len(numbers)
    # num_sum = sum(numbers)

    description = {
        # "length": num_length,
        # "sum": num_sum,
        "length": (num_length := len(numbers)),
        "sum": (num_sum := sum(numbers)),
        "mean": num_sum / num_length,
    }

    print(description)  # {'length': 8, 'sum': 35, 'mean': 4.375}


def do_calculations(numbers):
    # Using filter
    # results = filter(lambda value: value > 0, (_do_expensive_operation(num) for num in numbers))

    # Using a double list comprehension
    # results = [value for num in numbers for value in [_do_expensive_operation(num)] if value > 0]

    # Walrus operator improves code’s readability
    results = [value for num in numbers if (value := do_expensive_operation(num)) > 0]
    print(results)  # [3, 4, 2, 2]


def do_expensive_operation(n):
    return n - 5  # Yep, not very expensive...


# Assignment expressions can often be used to simplify while loops
def get_random_number():
    while (number := random.randint(1, 100)) < 50:
        pass
    print(number)


if __name__ == '__main__':
    numbers = [2, 8, 0, 1, 1, 9, 7, 7]

    get_numbers_descriptive_statistics(numbers)
    do_calculations(numbers)
    get_random_number()
