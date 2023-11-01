import tracemalloc
from functools import wraps
from typing import Callable


def get_memory_allocation(func: Callable) -> Callable:
    """
    Decorator.
    Measures the memory used by a function.
    """

    @wraps(func)
    def get_memory_allocation_wrapper(*args, **kwargs):
        tracemalloc.start()

        _ = func(*args, **kwargs)  # Allocate the result to keep the object in memory

        # noinspection PyShadowingNames
        size, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return size, peak

    return get_memory_allocation_wrapper
