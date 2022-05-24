#!/usr/bin/env python3
# _*_ coding:utf-8 _*

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
    print("\tList: {l", lst)

    position = lst.index("a")  # Returns the position of the first occurrence
    print(f"\tPosition: {position}")

    # noinspection PyBroadException
    try:
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
