#!/usr/bin/env python3

"""
A function defined inside another function is known as a nested function.
Nested functions are able to access variables of the enclosing scope.
"""


# Nested function
def outer_function(text):
    def inner_function():
        print(text)

    inner_function()


if __name__ == '__main__':
    outer_function('Hello World!')
