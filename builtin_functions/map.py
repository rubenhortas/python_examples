# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# map(function, iterables)

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    print("Map:")
    print(f"\tFruits: {fruits}")
    print(f"\tLengths of fruits: {list(map(len, fruits))}")
