#!/usr/bin/env python3

import time
from array import array
from functools import wraps
from io import StringIO

LIST_LENGTH = 10000
ITERATIONS = 1000


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        for i in range(1, ITERATIONS):
            func(*args, **kwargs)

        end_time = time.perf_counter()
        total_time = end_time - start_time

        return func.__name__, total_time

    return timeit_wrapper


@timeit
def naive_appending(lst):
    str_out = ""

    for item in lst:
        str_out = str_out + item


@timeit
def format_specifiers(lst):
    str_out = ""

    for item in lst:
        str_out = "%s%s" % (str_out, item)


@timeit
def string_format(lst):
    str_out = ""

    for item in lst:
        str_out = "{0}{1}".format(str_out, item)


@timeit
def string_format_without_positional_arguments(lst):  # python >= 3.1
    str_out = ""

    for item in lst:
        str_out = "{}{}".format(str_out, item)


@timeit
def character_array(lst):
    char_array = array("b")

    for item in lst:
        char_array.frombytes(bytes(item, "UTF-8"))


@timeit
def join_creating_list(lst):
    strings = []

    for item in lst:
        strings.append(item)

    "".join(strings)


@timeit
def join_without_creating_list(lst):
    "".join(lst)


@timeit
def write_pseudo_file(lst):
    file_str = StringIO()

    for item in lst:
        file_str.write(item)


@timeit
def fstrings(lst):
    str_out = ''

    for item in lst:
        str_out = f'{str_out}{item}'


if __name__ == '__main__':
    numbers = [str(i) for i in range(0, LIST_LENGTH)]
    results = {}
    pos = 1

    print("Starting measurements...")

    print("Concatenating with naive appending...")
    function_name, execution_time = naive_appending(numbers)
    results[function_name] = execution_time

    print("Concatenating with format specifiers...")
    function_name, execution_time = format_specifiers(numbers)
    results[function_name] = execution_time

    print("Concatenating with string format...")
    function_name, execution_time = string_format(numbers)
    results[function_name] = execution_time

    print("Concatenating with string format without positional arguments...")
    function_name, execution_time = string_format_without_positional_arguments(numbers)
    results[function_name] = execution_time

    print("Concatenating with character array...")
    function_name, execution_time = character_array(numbers)
    results[function_name] = execution_time

    print("Concatenating with join creating list...")
    function_name, execution_time = join_creating_list(numbers)
    results[function_name] = execution_time

    print("Concatenating with join without creating list...")
    function_name, execution_time = join_without_creating_list(numbers)
    results[function_name] = execution_time

    print("Concatenating with write pseudo file...")
    function_name, execution_time = write_pseudo_file(numbers)
    results[function_name] = execution_time

    print("Concatenating with fstrings...")
    function_name, execution_time = fstrings(numbers)
    results[function_name] = execution_time

    print("Results:")
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=False)

    for result in sorted_results:
        print(f"\t{pos} - {result[0]} {result[1]:.10f} secs")
        pos = pos + 1

    """"
    My results (sorted from faster to slowest):
        1 - join_without_creating_list
        2 - join_creating_list 
        3 - write_pseudo_file
        4 - naive_appending
        5 - character_array
        6 - fstrings
        6 - format_specifiers
        7 - string_format_without_positional_arguments
        8 - string_format
        
    * Sometimes write_pseudo_file is faster than join_creating_list
    """
