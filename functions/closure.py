#!/usr/bin/env python3

"""
A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
- It is a record that stores a function together with an environment
- A closure (unlike a plain function) allows the function to access those captured variables through the closure's
  copies of their values or references, even when the function is invoked outside their scope.

https://www.geeksforgeeks.org/python-closures/
"""


def outer_function(outer_text):
    def inner_function(inner_text):
        print(f'{outer_text} {inner_text}!')

    return inner_function


if __name__ == '__main__':
    f = outer_function('Hello')
    f('world')

    outer_function('Hello')('world')
