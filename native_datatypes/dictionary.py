#!/usr/bin/python3

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


def search(value, dict):
    if value in dict:
        print(f"{value} is in users")
    else:
        print(f"{value} is not in users")


def iterate(dict):
    print("Dictionary iteration:")

    for key in dict:
        print(f"\tkey: {key}\t value: {dict[key]}")


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

    print(f"Passwords: {users}")

    is_empty(users)
    is_empty(empty_dictionary)
    merge(users, new_users)
    comprehensions()
    search("root", users)
    iterate(users)
