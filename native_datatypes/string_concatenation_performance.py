#!/usr/bin/env python3

from array import array
from io import StringIO
from performance.execution_time import get_execution_time

LIST_LENGTH = 10000
ITERATIONS = 10000


@get_execution_time
def _execute(func, *args, **kwargs):
    for i in range(ITERATIONS):
        func(*args, **kwargs)


def _measure_function_time(func, *args, **kwargs) -> float:
    print(f"Measuring {func.__name__}...")

    total_time = _execute(func, *args, **kwargs)
    return total_time / ITERATIONS


def _naive_appending(lst):
    str_out = ""

    for item in lst:
        str_out = str_out + item


def _format_specifiers(lst):
    str_out = ""

    for item in lst:
        str_out = "%s%s" % (str_out, item)


def _string_format(lst):
    str_out = ""

    for item in lst:
        str_out = "{0}{1}".format(str_out, item)


def _string_format_without_positional_arguments(lst):  # python >= 3.1
    str_out = ""

    for item in lst:
        str_out = "{}{}".format(str_out, item)


def _character_array(lst):
    char_array = array("b")

    for item in lst:
        char_array.frombytes(bytes(item, "UTF-8"))


def _join_creating_list(lst):
    strings = []

    for item in lst:
        strings.append(item)

    "".join(strings)


def _join_without_creating_list(lst):
    "".join(lst)


def _write_pseudo_file(lst):
    file_str = StringIO()

    for item in lst:
        file_str.write(item)


def _fstrings(lst):
    str_out = ''

    for item in lst:
        str_out = f'{str_out}{item}'


if __name__ == '__main__':
    numbers = [str(i) for i in range(LIST_LENGTH)]
    results = {"Naive appending": _measure_function_time(_naive_appending, numbers),
               "Format specifiers": _measure_function_time(_format_specifiers, numbers),
               "String format": _measure_function_time(_string_format, numbers),
               "String format without positional arguments": _measure_function_time(
                   _string_format_without_positional_arguments, numbers),
               "Character array": _measure_function_time(_character_array, numbers),
               "Join creating list": _measure_function_time(_join_creating_list, numbers),
               "Join without creating list": _measure_function_time(_join_without_creating_list, numbers),
               "Write pseudo file": _measure_function_time(_write_pseudo_file, numbers),
               "Fstrings": _measure_function_time(_fstrings, numbers)}  # { function_name : avg_time }

    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=False)

    print("Results:")

    pos = 0

    for result in sorted_results:
        pos = pos + 1
        print(f"{pos}) {result[0]}: {result[1]:.5f} secs")

    """
    My results (sorted from faster to slowest):
        1) Join without creating list
        2) Join creating list
        3) Write pseudo file
        4) Character array
        5) Naive appending
        6) Fstrings
        7) Format specifiers
        8) String format without positional arguments
        9) String format
    """
