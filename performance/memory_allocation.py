import tracemalloc
from collections.abc import Callable
from functools import wraps


def get_memory_allocation(func: Callable) -> Callable:
    """
    Decorator.
    Measures the memory used by a function.
    """

    @wraps(func)
    def _get_memory_allocation(*args: object, **kwargs: object) -> tuple[int, int]:
        tracemalloc.start()

        _ = func(*args, **kwargs)  # Allocate the result to keep the object in memory

        # noinspection PyShadowingNames
        size, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return size, peak

    return _get_memory_allocation
