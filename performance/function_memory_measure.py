import tracemalloc
from functools import wraps


def trace(func):
    @wraps(func)
    def trace_wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        size, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{func.__name__}: current memory size: {size} KiB, peak memory size: {peak} KiB")
        return result

    return trace_wrapper


@trace
def create_list(size):
    lst = []

    for i in range(0, size - 1):
        lst.append(i)

    return lst


if __name__ == '__main__':
    create_list(100)
    create_list(1000)
