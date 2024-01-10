#!/usr/bin/env python3

"""
Closure are Nested functions that are able to access variables of the enclosing scope (even after the outer function is closed).
A closure occurs when a function has access to a local variable from an enclosing scope that has finished its execution.
"""

from typing import Callable


def _outer_function(outer_text: str) -> Callable[[str], None]:
    def inner_function(inner_text: str) -> None:
        greeting = '\\(^-^)/'
        print(f'{outer_text} {inner_text}! {greeting}')

    return inner_function


if __name__ == '__main__':
    f = _outer_function('Hello')
    f('world')
    # return: Hello world! \(^-^)/

    _outer_function('Hello')('world')
    # return: Hello world! \(^-^)/
