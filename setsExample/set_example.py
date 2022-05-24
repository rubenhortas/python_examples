# A set is an unordered “bag” of unique values. A single set can contain values of any immutable datatype.
# Once you have two sets, you can do standard set operations like union, intersection, and set difference

if __name__ == '__main__':
    # Create a set from a list
    lst = ["a", "b", "c"]
    list_set = set(lst)

    print("Create a set from a list:")
    print(f"\tList: {lst}")
    print(f"\tSet: {list_set}")

    # Merge two sets
    extended_set = {"c", "d", "e"}
    list_set.update(extended_set, list_set)

    print("Merging two sets:")
    print(f"\tExtended set: {extended_set}")
    print(f"\tUpdates list set: {list_set}")  # There is not duplicated values

    # Removing items from a set
    print("Removing 'e' from list_set:")
    list_set.remove("e")
    print(f"\t{list_set}")

    print("Removing a item that doesn't exist in the set")

    try:
        list_set.remove("e")  # Remove raises a KeyError exception if the value doesn't exist in the set
    except KeyError:
        print("\tThe item is not in the set")

    list_set.discard("e")  # Discard does nothing if the value doesn't exist in the set

    # Popping items
    # The pop() method removes a single value from a set and returns the value. However, since sets are unordered,
    # there is no “last” value in a set, so there is no way to control which value gets removed.
    # It is completely arbitrary.
    print("Popping a item from the set:")

    list_set.pop()

    print(f"\t{list_set}")

    # Check if a value is in the set
    print("Checking if 'a' is in the set")

    if "a" in list_set:
        print("\t'a' is in the set")  # Is in the set

    # Common set operations
    odd_set = {1, 3, 5, 7, 9}
    even_set = {2, 4, 6, 8, 10}
    mixed_set = {3, 4}
    union_set = odd_set.union(even_set)
    intersection_set = odd_set.intersection(mixed_set)
    # The difference() method returns a new set containing all the elements that are in odd_set but not in mixed_set
    difference_set = odd_set.difference(mixed_set)
    # The symmetric_difference() method returns a new set containing all the elements that are in exactly one of the sets.
    symmetric_difference_set = odd_set.symmetric_difference(mixed_set)

    print("Common set operations:")
    print(f"\todd set: {odd_set}")
    print(f"\teven set: {even_set}")
    print(f"\tmixed set: {mixed_set}")
    print(f"\tUnion of odd set and even set: {union_set}")
    print(f"\tIntersection of odd set and mixed set: {intersection_set}")
    print(f"\tDifference of odd set and mixed set: {difference_set}")
    print(f"\tSymmetric difference of odd set and mixed set: {symmetric_difference_set}")

    # Set comparison
    reversed_odd_set = {9, 7, 5, 3, 1}

    print("Comparing sets")
    if odd_set == reversed_odd_set:  # Any two sets that contain all the same values are considered equal.
        print(f"\t{odd_set} and {reversed_odd_set} are equals")  # Sets are equals

    # Set questions
    mini_odd_set = {1, 3}

    print("Set questions:")
    if mini_odd_set.issubset(odd_set):
        print(f"\t{mini_odd_set} is subset of {odd_set}")

    if odd_set.issuperset(mini_odd_set):
        print(f"\t{odd_set} is superset of {mini_odd_set}")

    # Sets in a boolean context
    # In a boolean context an empty set is False, otherwise is True
    empty_set = {}

    print("Sets in a boolean context:")

    if list_set:
        print(f"\t{list_set} is not empty")

    if not empty_set:
        print(f"\t{empty_set} is empty")
