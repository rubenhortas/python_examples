#!/usr/bin/env python3

# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.
# Example:
#   Input:  "Mr John Smith    ", 13
#   Output: "Mr%20John%20Smith"
# (!) We have to use a single string

INPUT = "Mr John Smith    "  # length = 17, "true" length = 13
INPUT_TRUE_LENGTH = 13


def _get_url(string: list, true_length: int) -> list:
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


if __name__ == '__main__':
    # We will use a list because, in python, strings are immutable
    url = _get_url(list(INPUT), INPUT_TRUE_LENGTH)

    print(f"\"{''.join(url)}\" -> {url} (length = {len(url)})")
    # return: "Mr%20John%20Smith" -> ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h'] (length = 17)
