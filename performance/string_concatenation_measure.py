#!/usr/bin/python3

from io import StringIO
from array import array
import timeit

ITEM_NUMBERS = 10000
ITERATIONS = 1000


def measure_time(fun):
    t_start = timeit.default_timer()

    for i in range(1, ITERATIONS):
        fun()

    t_end = timeit.default_timer()
    t_total = (t_end - t_start) / ITERATIONS

    return f"{t_total:.10f} {fun.__name__}"


def naive_appending():
    print("Concatenating with naive appending...")

    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = str_out + str(i)


def format_specifiers():
    # str_out = "%s %s" % (str_hello, str_my_friend)
    print("Concatenating with format specifiers...")

    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "%s%s" % (str_out, str(i))


def string_format():
    print("Concatenating with string format...")

    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "{0}{1}".format(str_out, str(i))


def string_format_without_positional_arguments():  # python >= 3.1
    print("Concatenating with string format without positional arguments...")

    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "{}{}".format(str_out, str(i))


def character_array():
    print("Concatenating with character array...")

    char_array = array("b")

    for i in range(1, ITEM_NUMBERS):
        char_array.frombytes(bytes(i))


def build_list():
    print("Concatenating with build list...")

    strings = []

    for i in range(1, ITEM_NUMBERS):
        strings.append(str(i))

    "".join(strings)


def write_pseudo_file():
    print("Concatenating with write pseudo file...")

    file_str = StringIO()

    for i in range(1, ITEM_NUMBERS):
        file_str.write(str(i))
        file_str.write(" ")


if __name__ == '__main__':
    average_times = []
    pos = 1

    print("Starting measurements...")
    average_times.append(measure_time(naive_appending))
    average_times.append(measure_time(format_specifiers))
    average_times.append(measure_time(string_format))
    average_times.append(measure_time(string_format_without_positional_arguments))
    average_times.append(measure_time(character_array))
    average_times.append(measure_time(build_list))
    average_times.append(measure_time(write_pseudo_file))

    print("Results:")
    sorted_averaged_times = sorted(average_times)

    for average_time in sorted_averaged_times:
        print(f"\t{pos} - {average_time}")
        pos = pos + 1

    print()

    """"
    My results (sorted by faster to slowest):
        1 - build_list
        2 - write_pseudo_file
        3 - naive_appending
        4 - format_specifiers
        5 - string_format_without_positional_arguments
        6 - string_format
        7 - character_array
    """
