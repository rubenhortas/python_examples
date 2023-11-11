#!/usr/bin/env python3

# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.
# Example:
#   Input:  "Mr John Smith    ", 13
#   Output: "Mr%20John%20Smith"
# (!) We have to use a single string


def get_url(string: list, true_length: int) -> list:
    # Time complexity: O(n)
    # Auxiliary space: O(1)
    spaces = 0

    for i in range(true_length - 1, 0, -1):
        if string[i] == ' ':
            spaces = spaces + 1

    index = (true_length + (2 * spaces)) - 1

    for i in range(true_length - 1, 0, -1):  # (start, stop, step)
        if string[i] != ' ':
            string[index] = string[i]
            index = index - 1
        else:
            string[index] = '0'
            index = index - 1

            string[index] = '2'
            index = index - 1

            string[index] = '%'
            index = index - 1

    return string


def get_url_pythonic(string: list, true_length: int) -> list:
    # Time complexity: O(n)
    # Auxiliary space: O(1)
    index = len(string)

    for i in reversed(range(true_length)):
        if string[i] == ' ':
            string[index - 3:index] = '%20'
            index = index - 3
        else:
            string[index - 1] = string[i]
            index = index - 1

    return string
