#!/usr/bin/env python3

import copy

EMPTY_DICT = {}

USERS = {
    "root": "r00t.h4x0r.p455",
    "guest": "",
    "bob": "123456",
    "Bob": "temp1234",  # Dictionary keys are case-sensitive
    "alice": "qwerty"
}

NEW_USERS = {
    "sysadmin": "r2@l.r00t",
    "anonymous": "anonymous"
}

USERS_COUNTER = {
    "root": 1,
    "users": 50,
    "admins": 4
}


def is_empty(dct: dict) -> None:
    # Dictionaries in a boolean context.
    # An empty dictionary is False otherwise is true.
    if dct:
        print(f"{dct} is not empty")
    else:
        print(f"{dct} is empty")


# noinspection PyShadowingNames
def merge(dict1: dict, dict2: dict) -> None:
    # Merging dictionaries.
    # Requires Python >= 3.5
    merged_dict = {**dict1, **dict2}

    print(f"Merged dict: {merged_dict}")


def comprehensions() -> None:
    powers = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}

    print(f"Powers: {powers}")


def check_key(dct: dict, key: str) -> None:
    if key in dct:
        print(f"'{key}' exists.")
    else:
        print(f"'{key}' does not exist.")


def get_value_with_default(dct: dict, key: str) -> None:
    value = dct.get(key, "default_value")
    print(f"The value of '{key}' is: {value}.")


def iterate(dct: dict) -> None:
    print("Dictionary: ", end="")

    for key in dct:
        print(f"{key}:{dct[key]}", end=", ")

    print()


def sort_by_value(dct: dict) -> None:
    # It is not possible to sort a dictionary, only to get a representation of a dictionary that is sorted.
    # Dictionaries are inherently orderless.
    # You need an ordered data type to represent sorted values.
    print(f"Sorting {dct} by values:")

    sorted_list = sorted(dct.items(), key=lambda item: item[1], reverse=True)  # sorted will return a list of tuples
    print(f"\t{sorted_list}")

    sorted_dict = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}  # returns a dictionary
    print(f"\t{sorted_dict}")


def do_shallow_copy(original_dict: dict) -> dict:
    # We will have new and independent object with the same contents as original_dict.
    # copy_dict still contains references to the original child objects stored in original_dict.
    # Child objects aren't copied. They are referenced.
    # When we modify one of the child objects in original_dict, this modification will be reflected in copy_dict.
    # noinspection PyShadowingNames
    copy_dict = {**original_dict}

    print(f"Shallow copy -> original dict.: {original_dict}, copy dict.: {copy_dict}")

    return copy_dict


def do_deep_copy(original_dict: dict) -> dict:
    # We will have two fully independent objects.
    # If we make a modification to one of the child objets in original_dict, this modification won't be reflected in copy_dict.
    # noinspection PyShadowingNames
    copy_dict = copy.deepcopy(original_dict)

    print(f"Deep copy -> original dict.: {original_dict}, copy dict.: {copy_dict}")

    return copy_dict


if __name__ == '__main__':
    # Dictionary with mutable objects for the shallow copy and deep copy examples.
    groups = {
        "root": ['root'],
        "nogroup": ['guest', 'anonymous'],
        "0g_h4x0r2": [],
    }

    print(f"Passwords: {USERS}")
    # return: Passwords: {'root': 'r00t.h4x0r.p455', 'guest': '', 'bob': '123456', 'Bob': 'temp1234', 'alice': 'qwerty'

    is_empty(USERS)
    # return: {'root': 'r00t.h4x0r.p455', 'guest': '', 'bob': '123456', 'Bob': 'temp1234', 'alice': 'qwerty'} is not empty

    is_empty(EMPTY_DICT)
    # return: {} is empty

    merge(USERS, NEW_USERS)
    # return: Merged dict: {'root': 'r00t.h4x0r.p455', 'guest': '', 'bob': '123456', 'Bob': 'temp1234', 'alice': 'qwerty', 'sysadmin': 'r2@l.r00t', 'anonymous': 'anonymous'}

    comprehensions()
    # return: Powers: {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

    check_key(USERS, "root")
    # return: 'root' exists.

    get_value_with_default(USERS, "ruben")
    # return: The value of 'ruben' is: default_value.

    iterate(USERS)
    # return: Dictionary: root:r00t.h4x0r.p455, guest:, bob:123456, Bob:temp1234, alice:qwerty,

    copy_dict = do_shallow_copy(groups)
    # return: Shallow copy -> original dict.: {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': []}, copy dict.: {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': []}

    # The modification in the original will be reflected in the copied dictionary.
    groups['0g_h4x0r2'].append('ctrl')
    groups['0g_h4x0r2'].append('demonsito')
    groups['0g_h4x0r2'].append('kaian')
    groups['0g_h4x0r2'].append('trazi')
    print(f"Modified shallow copy -> original dict. (modified!): {groups}, copy dict.: {copy_dict}")
    # return: Modified shallow copy -> original dict. (modified!): {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': ['ctrl', 'demonsito', 'kaian', 'trazi']}, copy dict.: {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': ['ctrl', 'demonsito', 'kaian', 'trazi']}

    copy_dict = do_deep_copy(groups)
    # return: Deep copy -> original dict.: {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': ['ctrl', 'demonsito', 'kaian', 'trazi']}, copy dict.: {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': ['ctrl', 'demonsito', 'kaian', 'trazi']}

    # The modification on the original dictionary will be NOT reflected in the copied dictionary.
    groups['0g_h4x0r2'].append('prospect')
    print(f"Modified shallow copy -> original dict.: {groups}, copy dict.: {copy_dict}")
    # return: Modified shallow copy -> original dict.: {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': ['ctrl', 'demonsito', 'kaian', 'trazi', 'prospect']}, copy dict.: {'root': ['root'], 'nogroup': ['guest', 'anonymous'], '0g_h4x0r2': ['ctrl', 'demonsito', 'kaian', 'trazi']}
