# A tuple is an immutable list. A tuple can not be changed in any way once it is created.
# Tuples doesn't have append(), extend(), insert(), remove(), or pop()
# Tuples are faster than lists
# With tuples you can protect data from read/write

if __name__ == '__main__':
    items_tuple = ("a", "b", "c")
    empty_tuple = ()

    # Tuples in a boolean context
    # An empty tuple is False otherwise is True
    if items_tuple:
        print(f"{items_tuple} is has items")

    if not empty_tuple:
        print(f"{empty_tuple} is empty")
