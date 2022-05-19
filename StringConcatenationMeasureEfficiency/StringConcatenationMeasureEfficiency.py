#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from io import StringIO
from array import array
import timeit

ITEM_NUMBERS = 10000
ITERATIONS = 100


def measure_time(fun):
    t_start = timeit.default_timer()

    for i in range(1, ITERATIONS):
        fun()

    t_end = timeit.default_timer()
    t_total = (t_end - t_start) / ITERATIONS

    return "%.10f %s" % (t_total, fun.__name__)


def naive_appending():
    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = str_out + str(i)


def format_specifiers():
    # str_out = "%s %s" % (str_hello, str_my_friend)
    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "%s%s" % (str_out, str(i))


def string_format():
    str_out = ""

    for i in range(1, ITEM_NUMBERS):
        str_out = "{0}{1}".format(str_out, str(i))


def character_array():
    char_array = array("b")

    for i in range(1, ITEM_NUMBERS):
        char_array.frombytes(bytes(i))


def build_list():
    strings = []

    for i in range(1, ITEM_NUMBERS):
        strings.append(str(i))


def write_pseudo_file():
    file_str = StringIO()

    for i in range(1, ITEM_NUMBERS):
        file_str.write(str(i))
        file_str.write(" ")


if __name__ == '__main__':
    times = []
    pos = 1

    print("Starting measurements...")

    print("Concatenating with naive appending...")
    times.append(measure_time(naive_appending))

    print("Concatenating with format specifiers...")
    times.append(measure_time(format_specifiers))

    print("Concatenating with string format...")
    times.append(measure_time(string_format))

    print("Concatenating with character array...")
    times.append(measure_time(character_array))

    print("Concatenating with build list...")
    times.append(measure_time(build_list))

    print("6 - Concatenating with write pseudo file...")
    times.append(measure_time(write_pseudo_file))

    sorted_times = sorted(times)

    for measure in sorted_times:
        print("{0} - {1}".format(pos, measure))
        pos = pos + 1

    print()

    """"
    My results (sorted by faster to slowest):
        1 - build_list
        2 - write_pseudo_file
        3 - format_specifiers
        4 - string_format
        5 - naive_appending
        6 - character_array
    """
