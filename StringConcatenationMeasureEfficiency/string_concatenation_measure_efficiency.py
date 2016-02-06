#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:        Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:       rubenhortas at gmail.com
@github:        http://github.com/rubenhortas
@license:       CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:          stringConcatenationMeasureEfficiency.py
@interpreter:   python 2.7
"""

# python 2.7
from StringIO import StringIO
from UserString import MutableString
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
    return "{0:0.10f} {1}".format(t_total, fun.__name__)


def naive_appending():
    str_out = ""
    for i in range(1, ITEM_NUMBERS):
        str_out = str_out + " " + str(i)


def format_specifiers():
    # str_out = '%s %s' % (str_hello, str_my_friend)
    str_out = ""
    for i in range(1, ITEM_NUMBERS):
        str_out = "%s %s" % (str_out, str(i))


def string_format():
    str_out = ""
    for i in range(1, ITEM_NUMBERS):
        str_out = "{0} {1}".format(str_out, str(i))


def mutable_string():
    str_out = MutableString()
    for i in range(1, ITEM_NUMBERS):
        str_out = str_out + str(i)


def character_array():
    char_array = array("c")
    for i in range(1, ITEM_NUMBERS):
        char_array.fromstring(str(i))
        char_array.fromstring(" ")


def build_list():
    strings = []
    for i in range(1, ITEM_NUMBERS):
        strings.append(str(i))
        strings.append(" ")


def write_pseudo_file():
    file_str = StringIO()
    for i in range(1, ITEM_NUMBERS):
        file_str.write(str(i))
        file_str.write(" ")

if __name__ == '__main__':

    l_time = []

    print "Starting measures...\n"

    l_time.append(measure_time(naive_appending))
    l_time.append(measure_time(format_specifiers))
    l_time.append(measure_time(string_format))
    l_time.append(measure_time(mutable_string))
    l_time.append(measure_time(character_array))
    l_time.append(measure_time(build_list))
    l_time.append(measure_time(write_pseudo_file))

    pos = 1
    for measure in sorted(l_time):
        print "{0} - {1}".format(pos, measure)
        pos = pos + 1

    print ""
