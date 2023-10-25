#!/usr/bin/env python3

"""
A closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding
in a language with first-class functions. Operationally, a closure is a record storing a function together
with an environment. The environment is a mapping associating each free variable of the function (variables that are
used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when
the closure was created. Unlike a plain function, a closure allows the function to access those captured variables
through the closure's copies of their values or references, even when the function is invoked outside their scope.
"""
from typing import Callable


def outer_function(outer_text: str) -> Callable[[str], None]:
    def inner_function(inner_text: str) -> None:
        greeting = "\\(^-^)/"
        print(f'{outer_text} {inner_text}! {greeting}')

    return inner_function


if __name__ == '__main__':
    f = outer_function('Hello')
    f('world')
    # return: Hello world! \(^-^)/

    outer_function('Hello')('world')
    # return: Hello world! \(^-^)/
