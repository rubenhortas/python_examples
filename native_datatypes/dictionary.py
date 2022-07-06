#!/usr/bin/env python3

EMPTY_DICT = {}

USERS = {
    "root": "r00t.h4x0r.p455",
    "guest": "",
    "bob": "123456",
    "alice": "qwerty"
}

NEW_USERS = {
    "sysadmin": "r2@l.r00t",
    "anonymous": "anonymous"
}

USERS_COUNTER = {
    "root": 1,
    "USERS": 50,
    "admins": 4
}


def add_users(users):
    # Modify dictionary values
    users["bob"] = "temporaryPassword"
    bob_password = users["bob"]
    print(f"New bob password: {bob_password}")

    # Dictionary keys are case-sensitive
    users["Bob"] = "temporary2"
    print(f"Updated Bob password: {users}")  # We have a new Bob


def is_empty(dct):
    # Dictionaries in a boolean context
    # An empty dictionary is False otherwise is true
    if dct:
        print(f"{dct} is not empty")
    else:
        print(f"{dct} is empty")


# noinspection PyShadowingNames
def merge(dict1, dict2):
    # Merging dictionaries Python >= 3.5
    merged_dict = {**dict1, **dict2}

    print(f"New USERS: {dict2}")
    print(f"Merged USERS: {merged_dict}")


def comprehensions():
    print("Dictionary comprehensions:")

    powers = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}

    print(f"\tPowers: {powers}")


def search(value, dct):
    if value in dct:
        print(f"{value} is in USERS")
    else:
        print(f"{value} is not in USERS")


def iterate(dct):
    print("Dictionary iteration:")

    for key in dct:
        print(f"\tkey: {key}\t value: {dct[key]}")


def sort_by_value(dct):
    # It is not possible to sort a dictionary, only to get a representation of a dictionary that is sorted.
    # Dictionaries are inherently orderless.
    # You need an ordered data type to represent sorted values.
    print(f"Sorting {dct} by values:")

    sorted_list = sorted(dct.items(), key=lambda item: item[1], reverse=True)  # sorted will return a list of tuples
    print(f"\t{sorted_list}")

    sorted_dict = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}  # returns a dictionary
    print(f"\t{sorted_dict}")


if __name__ == '__main__':
    print(f"Passwords: {USERS}")

    is_empty(USERS)
    is_empty(EMPTY_DICT)
    merge(USERS, NEW_USERS)
    comprehensions()
    search("root", USERS)
    iterate(USERS)
    sort_by_value(USERS_COUNTER)
