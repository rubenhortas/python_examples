#!/usr/bin/env python3

"""
A function defined inside another function is known as a nested function.
Nested functions are able to access variables of the enclosing scope.
"""


def outer_function(text: str) -> None:
    def nested_function() -> None:
        print(text)

    nested_function()


if __name__ == '__main__':
    outer_function('Hello World!')
    # return: Hello World!
