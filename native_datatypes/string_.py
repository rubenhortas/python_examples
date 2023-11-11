#!/usr/bin/env python3

from string import Template


def _multiline_strings() -> None:
    # Triple quotes allow printing in several lines with a single instruction
    print('''Multi line string
    in one instruction''')
    # return: Multi line string
    #             in one instruction

    print("""Another Multi line string
    in one instruction""")
    # return: Another Multi line string
    #             in one instruction 2


def _capitalize() -> None:
    # Return a capitalized version of the string.
    # More specifically, make the first character have upper case and the rest lower case.
    s1 = "my capitalized string"
    print(f"'{s1}' capitalized: '{s1.capitalize()}'")
    # return: 'my capitalized string' capitalized: 'My capitalized string'

    # Return a version of the string where each word is titlecased.
    # More specifically, words start with uppercased characters and all remaining cased characters have lower case.
    s2 = "my title string"
    print(f"'{s2}' titlecased: '{s2.title()}'")
    # return: 'my title string' titlecased: 'My Title String'


def _number_formatting() -> None:
    number_of_cats = 2

    print(f"I have {number_of_cats} cats")
    # return: I have 2 cats

    print(f"I have {number_of_cats:3d} cats")  # Three spaces
    # return: I have   2 cats

    print(f"I have {number_of_cats:03d} cats")  # Three spaces filled with 0s
    # return: I have 002 cats

    print(f"I have {number_of_cats:f} cats")
    # return: I have 2.000000 cats

    print(f"I have {number_of_cats:.2f} cats")
    # return: I have 2.00 cats


def _string_formatting() -> None:
    # Literal String Interpolation https://peps.python.org/pep-0498/
    one_argument = "one argument"
    print(f"f-string with {one_argument}")
    # return: f-string with one argument

    # %-formatting
    print("%%-formatting with %s" % one_argument)
    # return: %-formatting with one argument

    # str.format
    print("str.format with {0}".format(one_argument))
    # return: str.format with one argument

    # str.format Changed in version 3.1: The positional argument specifiers can be omitted for str.format()
    print("str.format with {}{}".format(one_argument, " or two..."))
    # return: str.format with one argument or two...

    # template
    str_template = Template("I have a template with $what")
    print(str_template.substitute(what=one_argument))
    # return: I have a template with one argument


def _string_formatting_types_based_on_placeholders() -> None:
    print(f"This is a {'left':<10} align.")
    # return: This is a left       align.

    print(f"This is a {'right':>10} align.")
    # return: This is a      right align.

    print(f"This is a {'center':^10} align.")
    # return: This is a   center   align.

    print(f"10 in binary is {10:b}")
    # return: 10 in binary is 1010

    print(f"0.55 is {0.55:.0%}")  # Percentage format
    # return: 0.55 is 55%

    print(f"I want {1000000:,}USD")  # Use comma as a thousand separator
    # return: I want 1,000,000USD


def _split() -> None:
    lorem_ipsum = "Lorem ipsum dolor sit amet"
    splitted_string = lorem_ipsum.split()  # To split on whitespace don’t have to give split any arguments

    print(f"'{lorem_ipsum}' splitted: {splitted_string}")
    # return: 'Lorem ipsum dolor sit amet' splitted: ['Lorem', 'ipsum', 'dolor', 'sit', 'amet']


def _join() -> None:
    lorem_ipsum = ["lorem", "ipsum", "dolor", "sit", "amet"]
    joined_string = " ".join(lorem_ipsum)

    print(f"{lorem_ipsum} joined: '{joined_string}'")
    # return: ['lorem', 'ipsum', 'dolor', 'sit', 'amet'] joined: 'lorem ipsum dolor sit amet'


def _reverse() -> None:
    # noinspection SpellCheckingInspection
    s = "REDRUM"
    reversed_s = s[::-1]  # slicing

    print(f"'{s}' backwards is '{reversed_s}'")
    # return: 'REDRUM' backwards is 'MURDER'


if __name__ == '__main__':
    _multiline_strings()
    _capitalize()
    _number_formatting()
    _string_formatting()
    _string_formatting_types_based_on_placeholders()
    _split()
    _join()
    _reverse()
