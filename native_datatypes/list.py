#!/usr/bin/env python3

EMPTY_LIST = []


# Add type hint to lst causes IDE warnings.
def add_items(lst) -> list:
    lst = lst + ['a']
    lst.append(1)  # In a list items don't need to be the same type
    lst.extend(['b', 2])
    lst.insert(0, True)

    print(f'List: {lst}')

    return lst


def search(lst: list, value) -> None:
    if value in lst:
        print(f'\'{value}\' is in the list')
    else:
        print(f'\'{value}\' is not in the list')


def get_value_position(lst: list, value) -> None:
    try:
        print(f'Position of {value}: {lst.index(value)}')  # Returns the position of the first occurrence
    except ValueError:
        print(f'{value} not found')


def get_value_by_position(lst: list, position: int) -> None:
    # A negative index accesses items from the end of the list counting backwards.
    # Negative index are valid, so raises an exception if the item is not found.
    try:
        print(f'Item in {position}: {lst[position]}')
    except IndexError:
        print(f'Position {position} not found')


def popping(lst: list) -> None:
    lst.pop()

    print(f'{lst}')


def is_empty(lst: list) -> None:
    # Empty list is false otherwise is true
    if lst:
        print(f'{lst} is not empty')
    else:
        print(f'{lst} is empty')


def comprehensions() -> None:
    numbers = [i for i in range(10)]
    even_numbers = [i for i in range(10) if i % 2 == 0]  # [ expression for item in list if conditional ]

    print(f'numbers: {numbers}, even numbers: {even_numbers}')


def reverse() -> None:
    numbers = [i for i in range(10)]
    reversed_numbers = numbers[::-1]

    print(f'{numbers} backwards is {reversed_numbers}')


def join() -> None:
    lst1 = ['a', 'b', 'c']
    lst2 = ['dct', 'e', 'f']

    joined_list_1 = lst1 + lst2
    lst1.extend(lst2)  # Adds lst2 at the end of lst1

    print(f'Join {lst1} and {lst2}')
    print(f'Join with +: {joined_list_1}')
    print(f'Join with extend: {lst1}')


# noinspection PyShadowingBuiltins
def slice() -> None:
    # Lst[ Initial : End : IndexJump ]
    numbers = [i for i in range(10)]

    print(f'{{lst[0:5]}}: {numbers[0:5]}')  # [0, 1, 2, 3, 4]

    # Negative Indexes
    # Index -1 represents the last element and -n represents the first element
    print(f'{{lst[-5::1]}}: {numbers[-5::1]}')  # [5, 6, 7, 8, 9]

    print(f'{{lst[::2]}}: {numbers[::2]}')  # [0, 2, 4, 6, 8]

    # List slicing can be used to delete elements from a list
    new_list = numbers[:2] + numbers[-2:]  # [0, 1, 8, 9]
    print(f'new_list = {new_list}')


if __name__ == '__main__':
    item_list = []

    item_list = add_items(item_list)
    # return: List: [True, 'a', 1, 'b', 2]

    search(item_list, 'a')
    # return: 'a' is in the list

    get_value_position(item_list, 'a')
    # return: Position of a: 1

    get_value_position(item_list, 'non_existing_value')
    # return: non_existing_value not found

    get_value_by_position(item_list, -1)
    # return: Item in -1: 2

    get_value_by_position(EMPTY_LIST, -1)
    # return: Position -1 not found

    popping(item_list)
    # return: [True, 'a', 1, 'b']

    is_empty(item_list)
    # return: [True, 'a', 1, 'b'] is not empty

    is_empty(EMPTY_LIST)
    # return: [] is empty

    comprehensions()
    # return: numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], even numbers: [0, 2, 4, 6, 8]

    reverse()
    # return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] backwards is [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    join()
    # return: Join ['a', 'b', 'c', 'dct', 'e', 'f'] and ['dct', 'e', 'f']
    #         Join with +: ['a', 'b', 'c', 'dct', 'e', 'f']
    #         Join with extend: ['a', 'b', 'c', 'dct', 'e', 'f']

    slice()
    # return: {lst[0:5]}: [0, 1, 2, 3, 4]
    #         {lst[-5::1]}: [5, 6, 7, 8, 9]
    #         {lst[::2]}: [0, 2, 4, 6, 8]
    #         new_list = [0, 1, 8, 9]
