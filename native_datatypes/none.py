#!/usr/bin/env python3
# ruff: noqa
# noinspection PyComparisonWithNone

"""
None is a null number.
Comparing None to anything other than None will always return False.
None is the only null number.
It has its own datatype (NoneType).
You can assign None to any variable, but you can not create other NoneType objects.
"""

if __name__ == "__main__":
    print(f"None == False -> {None == False}")  # False
    print(f"None == 0     -> {None == 0}")  # False
    print(f"None == ''    -> {None == ''}")  # False
    print(f"None == []    -> {None == []}")  # False

    # noinspection PyComparisonWithNone
    print(f"None == None  -> {None == None}")  # True
    print(f"None is None  -> {None is None}")  # True
    print(f"None != False -> {None != False}")  # True
    print(f"None is not 0 -> {None is not 0}")  # True

    # In a boolean context None is False
    if not None:
        print("In a boolean context None is always False")

    # noinspection PyStringConversionWithoutDunderMethod
    print(f"type(None)           -> {type(None)}")
    print(f"isinstance(None, type(None)) -> {isinstance(None, type(None))}")
