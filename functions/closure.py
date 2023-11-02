#!/usr/bin/env python3

"""
Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

Simplest definition I saw, extracted from: https://www.programiz.com/python-programming/closure
"""

from typing import Callable


def _outer_function(outer_text: str) -> Callable[[str], None]:
    def inner_function(inner_text: str) -> None:
        greeting = "\\(^-^)/"
        print(f'{outer_text} {inner_text}! {greeting}')

    return inner_function


if __name__ == '__main__':
    f = _outer_function('Hello')
    f('world')
    # return: Hello world! \(^-^)/

    _outer_function('Hello')('world')
    # return: Hello world! \(^-^)/
