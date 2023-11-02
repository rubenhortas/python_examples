#!/usr/bin/env python3

"""
A set is an unordered “bag” of unique values.
Sets are used to store multiple items in a single variable.
A single set can contain values of any immutable datatype.
Set items are unordered, unchangeable, and do not allow duplicate values.
Once you have two sets, you can do standard set operations like union, intersection, and set difference.
"""

CHARS = ["a", "b", "c"]
CHAR_2 = {"c", "dct", "e"}
EMPTY = set()  # To create an empty set you have to use set(), not {}; the latter creates an empty dictionary.
ODD = {1, 3, 5, 7, 9}
MINI_ODD = {1, 3}
REVERSED_ODD = {9, 7, 5, 3, 1}
EVEN = {2, 4, 6, 8, 10}
NUMBERS = {3, 4}


def create_from_list(lst: list) -> set:
    list_set = set(lst)

    print(f"List: {lst} -> set: {list_set}")

    return list_set


def merge(set1: set, set2: set) -> set:
    print(f"Merging {set2} into {set1}:", end=' ')

    set1.update(set1, set2)

    print(f"{set1}")  # There is not duplicated values

    return set1


# noinspection PyShadowingBuiltins
def remove_item(set: set, item: str) -> None:
    print(f"Removing '{item}' from {set}:", end=' ')

    try:
        set.remove(item)  # Remove raises a KeyError exception if the number doesn't exist in the set
    except KeyError:
        pass

    print(f"{set}")


# noinspection PyShadowingBuiltins
def discard_item(set: set, item: str) -> None:
    print(f"Discarding '{item}' from {set}:", end=' ')

    set.discard(item)  # Discard does nothing if the number doesn't exist in the set

    print(f"{set}")


# noinspection PyShadowingBuiltins
def pop(set: set) -> None:
    # The pop() method removes a single number from a set and returns the number. However, since sets are unordered,
    # there is no “last” number in a set, so there is no way to control which number gets removed.
    # It is completely arbitrary.
    print(f"Popping an item from {set}:", end=' ')

    set.pop()

    print(f"{set}")


# noinspection PyShadowingBuiltins
def get_value(set: set, value: str) -> None:
    if value in set:
        print(f"'{value}' is in {set}")
    else:
        print(f"'{value}' 'is not in {set}")


def common_operations(set1: set, set2: set, set3: set):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set3)

    # The difference() method returns a new set containing all the elements that are in ODD_SET but not in MIXED_SET
    difference_set = set1.difference(set3)

    # The symmetric_difference() method returns a new set containing all the elements that are in exactly one of the sets.
    symmetric_difference_set = set1.symmetric_difference(set3)

    print("Common set operations:")
    print(f"\todd set: {set1}")
    print(f"\teven set: {set2}")
    print(f"\tmixed set: {set3}")
    print(f"\tUnion of odd set and even set: {union_set}")
    print(f"\tIntersection of odd set and mixed set: {intersection_set}")
    print(f"\tDifference of odd set and mixed set: {difference_set}")
    print(f"\tSymmetric difference of odd set and mixed set: {symmetric_difference_set}")


def compare(set1: set, set2: set) -> None:
    if set1 == set2:  # Any two sets that contain all the same values are considered equal.
        print(f"{set1} and {set2} are equals")
    else:
        print(f"{set1} and {set2} are different")


def is_subset(set1: set, set2: set) -> None:
    if set1.issubset(set2):
        print(f"{set1} is a subset of {set2}")
    else:
        print(f"{set1} is not a subset of {set2}")


def is_superset(set1: set, set2: set) -> None:
    if set1.issuperset(set2):
        print(f"{set1} is a superset of {set2}")
    else:
        print(f"{set1} is not a superset of {set2}")


# noinspection PyShadowingBuiltins
def is_empty(set: set) -> None:
    if set:  # In a boolean context an empty set is False, otherwise is True
        print(f"{set} is not empty")
    else:
        print(f"{set} is empty")


# noinspection PyShadowingBuiltins
def get_max(set: set) -> None:
    print(f"The maximum item in {set} is '{max(set)}'")


# noinspection PyShadowingBuiltins
def get_min(set: set) -> None:
    print(f"The minimum item in {set} is '{min(set)}'")


if __name__ == '__main__':
    char_1 = create_from_list(CHARS)
    # return: List: ['a', 'b', 'c'] -> set: {'c', 'b', 'a'}

    merged_set = merge(char_1, CHAR_2)
    # return: Merging {'c', 'dct', 'e'} into {'b', 'a', 'c'}: {'b', 'c', 'dct', 'a', 'e'}

    remove_item(merged_set, 'e')
    # return: Removing 'e' from {'e', 'c', 'dct', 'b', 'a'}: {'c', 'dct', 'b', 'a'}

    discard_item(merged_set, 'ee')
    # return: Discarding 'ee' from {'a', 'c', 'b', 'dct'}: {'a', 'c', 'b', 'dct'}

    pop(merged_set)
    # return: Popping an item from {'b', 'a', 'c', 'dct'}: {'a', 'c', 'dct'}

    get_value(merged_set, 'a')
    # return: 'a' is in {'b', 'a', 'c'}

    common_operations(ODD, EVEN, NUMBERS)
    # return: Common set operations:
    #   odd set: {1, 3, 5, 7, 9}
    # 	even set: {2, 4, 6, 8, 10}
    # 	mixed set: {3, 4}
    # 	Union of odd set and even set: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # 	Intersection of odd set and mixed set: {3}
    # 	Difference of odd set and mixed set: {1, 5, 9, 7}
    # 	Symmetric difference of odd set and mixed set: {1, 4, 5, 7, 9}

    compare(ODD, REVERSED_ODD)
    # return: {1, 3, 5, 7, 9} and {1, 3, 5, 7, 9} are equals

    is_subset(MINI_ODD, ODD)
    # return: {1, 3} is a subset of {1, 3, 5, 7, 9}

    is_superset(ODD, MINI_ODD)
    # return: {1, 3, 5, 7, 9} is a superset of {1, 3}

    is_empty(ODD)
    # return: {1, 3, 5, 7, 9} is not empty

    is_empty(EMPTY)
    # return: set() is empty

    get_max(ODD)
    # return: The maximum item in {1, 3, 5, 7, 9} is '9'

    get_min(ODD)
    # return: The minimum item in {1, 3, 5, 7, 9} is '1'
