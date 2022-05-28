#!/usr/bin/python3

def initialize_users():
    return users


def add_users(users):
    # Modify dictionary values
    users["bob"] = "temporaryPassword"
    bob_password = users["bob"]
    print(f"New bob password: {bob_password}")

    # Dictionary keys are case-sensitive
    users["Bob"] = "temporary2"
    print(f"Updated Bob password: {users}")  # We have a new Bob


def check_empty(users, empty):
    # Dictionaries in a boolean context
    # An empty dictionary is False otherwise is true
    if users:
        print(f"{users} is not empty")

    if not empty:
        print(f"{empty_dictionary} is empty")


def merge(users, new_users):
    # Merging dictionaries Python >= 3.5
    merged_users = {**users, **new_users}

    print(f"New users: {new_users}")
    print(f"Merged users: {merged_users}")


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

    check_empty(users, empty_dictionary)
    merge(users, new_users)
