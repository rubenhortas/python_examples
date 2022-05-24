#!/usr/bin/python3

if __name__ == '__main__':
    lst = []

    # Adding items
    lst = lst + ["a"]
    lst.append(1)  # In a lst items don"t need to be the same type
    lst.extend(["b", 2])
    lst.insert(0, True)

    print(f"List: {lst}")

    # Searching for values
    print("Searching for values")
    if "a" in lst:
        print("\tThe value is in the lst")

    lst.append("a")
    print(f"\tList: {lst}")

    position = lst.index("a")  # Returns the position of the first occurrence
    print(f"\tPosition: {position}")

    # noinspection PyBroadException
    try:
        # A negative index accesses items from the end of the list counting backwards.
        # Negative index are valid, so raises an exception if the item is not
        # found
        print(f"\tItem in -1 position: {lst[-1]}")
        position = lst.index(False)
    except:
        print("\tItem not found")

    # Popping
    print("Popping")
    print(f"\t{lst}")
    lst.pop()
    print(f"\t{lst}")

    # Lists in a boolean context
    # Empty lists are false otherwise is true
    empty_list = []
    print("Lists in a boolean context:")
    if lst:
        print(f"\t{lst} is not empty")

    if not empty_list:
        print(f"\t{empty_list} is empty")
