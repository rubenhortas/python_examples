#!/usr/bin/python 3
import time
from functools import wraps
from typing import Callable


def get_execution_time(func: Callable) -> Callable:
    """
    Decorator.
    Measures the execution time of a function.
    """

    @wraps(func)
    def get_execution_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        func(*args, **kwargs)

        end_time = time.perf_counter()
        total_time = end_time - start_time

        return total_time

    return get_execution_time_wrapper