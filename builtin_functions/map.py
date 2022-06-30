# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# map(function, iterables)

FRUITS = ['apple', 'banana', 'cherry']

if __name__ == '__main__':
    print("Map:")
    print(f"\tFruits: {FRUITS}")
    print(f"\tLengths of fruits: {list(map(len, FRUITS))}")
