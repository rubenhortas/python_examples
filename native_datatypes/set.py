#!/usr/bin/env python3

# A set is an unordered “bag” of unique values. A single set can contain values of any immutable datatype.
# Once you have two sets, you can do standard set operations like union, intersection, and set difference

# noinspection PyShadowingNames
def create_from_list(lst):
    print("Create a set from a list:")
    print(f"\tList: {lst}")

    list_set = set(lst)

    print(f"\tSet: {list_set}")

    return set(list_set)


def merge(set1, set2):
    print("Merging two sets:")
    print(f"\tset1: {set1}")
    print(f"\tset2: {set2}")

    set1.update(set1, set2)

    print(f"\tUpdated set1: {set1}")  # There is not duplicated values

    return set1


# noinspection PyShadowingBuiltins
def remove_item(set, item):
    # Removing items from a set
    print(f"Removing 'e' from {set}:")

    try:
        set.remove(item)  # Remove raises a KeyError exception if the value doesn't exist in the set
    except KeyError:
        print(f"\t{item} is not in {set}")

    set.discard("e")  # Discard does nothing if the value doesn't exist in the set


# noinspection PyShadowingBuiltins
def pop(set):
    # Popping items
    # The pop() method removes a single value from a set and returns the value. However, since sets are unordered,
    # there is no “last” value in a set, so there is no way to control which value gets removed.
    # It is completely arbitrary.
    print("Popping a item from the set:")

    set.pop()

    print(f"\t{set}")


# noinspection PyShadowingBuiltins
def search_value(set, value):
    print(f"Checking if {value} is in {set}")

    if value in set:
        print(f"\t{value} is in the set")
    else:
        print(f"\t{value} is not in the set")


def common_operations(set1, set2, set3):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set3)
    # The difference() method returns a new set containing all the elements that are in odd_set but not in mixed_set
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


def compare(set1, set2):
    print("Comparing sets")

    if set1 == set2:  # Any two sets that contain all the same values are considered equal.
        print(f"\t{set1} and {set2} are equals")  # Sets are equals


def is_subset(set1, set2):
    if set1.issubset(set2):
        print(f"\t{set1} is subset of {set2}")


def is_superset(set1, set2):
    if set1.issuperset(set2):
        print(f"\t{set1} is superset of {set2}")


# noinspection PyShadowingBuiltins
def is_empty(set):
    # In a boolean context an empty set is False, otherwise is True
    if set:
        print(f"\t{set} is not empty")


# noinspection PyShadowingBuiltins
def get_max(set):
    print(f"The biggest item in {set} is {max(set)}")


if __name__ == '__main__':
    lst = ["a", "b", "c"]
    char_set_two = {"c", "dct", "e"}
    odd_set = {1, 3, 5, 7, 9}
    mini_odd_set = {1, 3}
    reversed_odd_set = {9, 7, 5, 3, 1}
    even_set = {2, 4, 6, 8, 10}
    mixed_set = {3, 4}
    empty_set = {}

    char_set = create_from_list(lst)
    merged_set = merge(char_set, char_set_two)
    remove_item(merged_set, 'e')
    pop(merged_set)
    search_value(merged_set, 'a')
    common_operations(odd_set, even_set, mixed_set)
    compare(odd_set, reversed_odd_set)
    is_subset(mini_odd_set, odd_set)
    is_superset(odd_set, mini_odd_set)
    is_empty(odd_set)
    is_empty(empty_set)
    get_max(odd_set)
