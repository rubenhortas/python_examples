#!/usr/bin/python3

if __name__ == '__main__':
    users = {
        "root": "r00t.h4x0r.p455",
        "guest": "",
        "bob": "123456",
        "alice": "qwerty"
    }

    print(f"Passwords: {users}")

    users["bob"] = "temporaryPassword"
    bob_password = users["bob"]
    print(f"New bob password: {bob_password}")

    # Dictionary keys are case-sensitive
    users["Bob"] = "temporary2"
    print(f"Updated Bob password: {users}")  # We have a new Bob

    # Dictionaries in a boolean context
    # An empty dictionary is False otherwise is true
    empty_dictionary = {}

    if users:
        print(f"{users} is not empty")

    if not empty_dictionary:
        print(f"{empty_dictionary} is empty")
