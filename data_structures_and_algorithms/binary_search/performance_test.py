import tracemalloc

from data_structures_and_algorithms.binary_search import binary_search, binary_search_traditional

if __name__ == '__main__':
    numbers = [9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]
    number = 5

    tracemalloc.start()
    binary_search.locate_position(numbers, number)
    size, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"binary_search: current memory size: {size} KiB, peak memory size: {peak} KiB")

    tracemalloc.start()
    binary_search_traditional.locate_position(numbers, number)
    size, peak = tracemalloc.get_traced_memory()
    print(f"binary_search_traditional: current memory size: {size} KiB, peak memory size: {peak} KiB")
    tracemalloc.stop()
