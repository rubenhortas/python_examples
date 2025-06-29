#!/usr/bin/env python3

"""
A function defined inside another function is known as a nested function.
If a nested function don't access variables that are local to enclosing scopes isn't a closure.
"""


def outer_function(text: str) -> None:
    def nested_function() -> None:
        print(text)

    nested_function()


if __name__ == '__main__':
    outer_function('Hello World!')
    # return: Hello World!
