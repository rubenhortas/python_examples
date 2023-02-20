#!/usr/bin/env python3

EMPTY_LIST = []


def add_items(lst):
    print("Adding items")

    lst = lst + ["a"]
    lst.append(1)  # In a list items don"t need to be the same type
    lst.extend(["a", 2])
    lst.insert(0, True)

    print(f"\tList: {lst}")

    return lst


def search(lst, value):
    # Searching for values
    print("Searching for values")

    if value in lst:
        print(f"\t{value} is in the list")

    print(f"\tList: {lst}")


def get_value_position(lst, value):
    print(f"Getting value position in {lst}:")

    try:
        print(f"\tPosition of {value}: {item_list.index(value)}")  # Returns the position of the first occurrence
    except ValueError:
        print(f"\t{value} not found")


def get_value_by_position(lst, position):
    # A negative index accesses items from the end of the list counting backwards.
    # Negative index are valid, so raises an exception if the item is not found.
    print(f"Getting value in position {position} in {lst}:")

    try:
        print(f"\tItem in {position}: {lst[position]}")
    except IndexError:
        print(f"\tPosition {position} not found")


def popping(lst):
    print("Popping:")
    print(f"\t{lst}")

    lst.pop()

    print(f"\t{lst}")


def is_empty(lst):
    # Empty lists are false otherwise is true
    print("Lists in a boolean context:")

    if lst:
        print(f"\t{lst} is not empty")
    else:
        print(f"\t{lst} is empty")


def comprehensions():
    # [ expression for item in list if conditional ]
    print("List comprehensions:")

    numbers = [i for i in range(0, 10)]
    even_numbers = [i for i in range(0, 10) if i % 2 == 0]

    print(f"\tnumbers: {numbers}")
    print(f"\teven numbers: {even_numbers}")


def reverse():
    numbers = [i for i in range(0, 10)]
    reversed_numbers = numbers[::-1]

    print(f"Reversing: {numbers} backwards is {reversed_numbers}")


def join():
    print("Join lists:")

    lst1 = ['a', 'b', 'c']
    lst2 = ['dct', 'e', 'f']

    joined_list_1 = lst1 + lst2
    lst1.extend(lst2)  # Adds lst2 to end of lst1

    print(f"\tJoin {lst1} and {lst2}")
    print(f"\tJoin with +: {joined_list_1}")
    print(f"\tJoin with extend: {lst1}")


def slicing():
    # Lst[ Initial : End : IndexJump ]
    numbers = [i for i in range(0, 10)]

    print(f"Slicing {numbers}:")
    print(f"\t{{lst[0:5]}}: {numbers[0:5]}")  # [0, 1, 2, 3, 4]

    # Negative Indexes
    # Index -1 represents the last element and -n represents the first element
    print(f"\t{{lst[-5::1]}}: {numbers[-5::1]}")  # [5, 6, 7, 8, 9]

    print(f"\t{{lst[::2]}}: {numbers[::2]}")  # [0, 2, 4, 6, 8]

    # List slicing can be used to delete elements from a list
    new_list = numbers[:2] + numbers[-2:]  # [0, 1, 8, 9]
    print(f"\tnew_list = {new_list}")


if __name__ == '__main__':
    item_list = []

    print(f"List: {item_list}")

    item_list = add_items(item_list)
    search(item_list, 'a')
    get_value_position(item_list, 'a')
    get_value_position(item_list, 'non_existing_value')
    get_value_by_position(item_list, -1)
    get_value_by_position(EMPTY_LIST, -1)
    popping(item_list)
    is_empty(item_list)
    is_empty(EMPTY_LIST)
    comprehensions()
    reverse()
    join()
    slicing()
