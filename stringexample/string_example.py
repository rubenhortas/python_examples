#!/usr/bin/python3

from string import Template


def multiline_strings():
    print("Multiline strings:")
    # Triple quotes allow printing in several lines with a single instruction
    print('''Multi line string
    in one instruction 1''')
    print()

    print("""Multi line string
    in one instruction 2""")
    print()


def capitalizing_strings():
    print("Capitalizing strings:")
    # Return a capitalized version of the string.
    # More specifically, make the first character have upper case and the rest lower case.
    print("my capitalized string".capitalize())

    # Return a version of the string where each word is titlecased.
    # More specifically, words start with uppercased characters and all remaining cased characters have lower case
    print("my title string".title())
    print()


def number_formatting():
    # Number format examples
    number_of_cats = 2
    print("Number formatting:")
    print(f"I have {number_of_cats} cats")
    print(f"I have {number_of_cats:3d} cats")  # Three spaces
    print(f"I have {number_of_cats:03d} cats")  # Three spaces filled with 0s
    print(f"I have {number_of_cats:f} cats")
    print(f"I have {number_of_cats:.2f} cats")
    print()


def string_formatting():
    print("String formatting:")
    # String format examples
    # Literal String Interpolation https://peps.python.org/pep-0498/
    str_one_argument = "one argument"
    print(f"f-string with {str_one_argument}")

    # %-formatting
    print("%%-formatting with %s" % str_one_argument)

    # str.format
    print("str.format with {0}".format(str_one_argument))
    # Changed in version 3.1: The positional argument specifiers can be omitted for str.format()
    print("str.format with {}{}".format(str_one_argument, " or two.."))

    # template
    s = Template("I have a template with $what")
    print(s.substitute(what=str_one_argument))


if __name__ == '__main__':
    multiline_strings()
    capitalizing_strings()
    number_formatting()
    string_formatting()
