#!/usr/bin/env python3

import time
from array import array
from functools import wraps
from io import StringIO

ITEM_NUMBERS = 10000
ITERATIONS = 1000


def timeit(func):
    @wraps(func)
    def timeit_wrapper():
        start_time = time.perf_counter()

        for i in range(1, ITERATIONS):
            func()

        end_time = time.perf_counter()
        total_time = end_time - start_time

        return func.__name__, total_time

    return timeit_wrapper


@timeit
def naive_appending():
    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = str_out + str(i)


@timeit
def format_specifiers():
    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "%s%s" % (str_out, str(i))


@timeit
def string_format():
    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "{0}{1}".format(str_out, str(i))


@timeit
def string_format_without_positional_arguments():  # python >= 3.1
    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "{}{}".format(str_out, str(i))


@timeit
def character_array():
    char_array = array("b")

    for i in range(1, ITEM_NUMBERS):
        char_array.frombytes(bytes(i))


@timeit
def build_list():
    strings = []

    for i in range(1, ITEM_NUMBERS):
        strings.append(str(i))

    "".join(strings)


@timeit
def write_pseudo_file():
    file_str = StringIO()

    for i in range(1, ITEM_NUMBERS):
        file_str.write(str(i))
        file_str.write(" ")


if __name__ == '__main__':
    results = {}
    pos = 1

    print("Starting measurements...")

    print("Concatenating with naive appending...")
    function_name, execution_time = naive_appending()
    results[function_name] = execution_time

    print("Concatenating with format specifiers...")
    function_name, execution_time = format_specifiers()
    results[function_name] = execution_time

    print("Concatenating with string format...")
    function_name, execution_time = string_format()
    results[function_name] = execution_time

    print("Concatenating with string format without positional arguments...")
    function_name, execution_time = string_format_without_positional_arguments()
    results[function_name] = execution_time

    print("Concatenating with character array...")
    function_name, execution_time = character_array()
    results[function_name] = execution_time

    print("Concatenating with build list...")
    function_name, execution_time = build_list()
    results[function_name] = execution_time

    print("Concatenating with write pseudo file...")
    function_name, execution_time = write_pseudo_file()
    results[function_name] = execution_time

    print("Results:")
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=False)

    for result in sorted_results:
        print(f"\t{pos} - {result[0]} {result[1]:.10f} secs")
        pos = pos + 1

    """"
    My results (sorted from faster to slowest):
       1 - naive_appending
       2 - build_list
       3 - write_pseudo_file
       4 - format_specifiers
       5 - string_format_without_positional_arguments
       6 - string_format
       7 - character_array
    """
