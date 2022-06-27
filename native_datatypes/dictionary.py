#!/usr/bin/env python3

# noinspection PyShadowingNames
def add_users(users):
    # Modify dictionary values
    users["bob"] = "temporaryPassword"
    bob_password = users["bob"]
    print(f"New bob password: {bob_password}")

    # Dictionary keys are case-sensitive
    users["Bob"] = "temporary2"
    print(f"Updated Bob password: {users}")  # We have a new Bob


# noinspection PyShadowingBuiltins
def is_empty(dict):
    # Dictionaries in a boolean context
    # An empty dictionary is False otherwise is true
    if dict:
        print(f"{dict} is not empty")
    else:
        print(f"{dict} is empty")


# noinspection PyShadowingNames
def merge(dict1, dict2):
    # Merging dictionaries Python >= 3.5
    merged_dict = {**dict1, **dict2}

    print(f"New users: {dict2}")
    print(f"Merged users: {merged_dict}")


def comprehensions():
    print("Dictionary comprehensions:")

    powers = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}

    print(f"\tPowers: {powers}")


def search(value, dct):
    if value in dct:
        print(f"{value} is in users")
    else:
        print(f"{value} is not in users")


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
    empty_dictionary = {}
    users = {
        "root": "r00t.h4x0r.p455",
        "guest": "",
        "bob": "123456",
        "alice": "qwerty"
    }
    new_users = {
        "sysadmin": "r2@l.r00t",
        "anonymous": "anonymous"
    }

    users_counter = {
        "root": 1,
        "users": 50,
        "admins": 4
    }

    print(f"Passwords: {users}")

    is_empty(users)
    is_empty(empty_dictionary)
    merge(users, new_users)
    comprehensions()
    search("root", users)
    iterate(users)
    sort_by_value(users_counter)
