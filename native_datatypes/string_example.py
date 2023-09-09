#!/usr/bin/env python3

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


def capitalize():
    print("Capitalizing strings:")

    # Return a capitalized version of the string.
    # More specifically, make the first character have upper case and the rest lower case.
    print("my capitalized string".capitalize())

    # Return a version of the string where each word is titlecased.
    # More specifically, words start with uppercased characters and all remaining cased characters have lower case
    print("my title string".title())
    print()


def number_formatting():
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

    # Literal String Interpolation https://peps.python.org/pep-0498/
    str_one_argument = "one argument"
    print(f"f-string with {str_one_argument}")

    # %-formatting
    print("%%-formatting with %s" % str_one_argument)

    # str.format
    print("str.format with {0}".format(str_one_argument))

    # str.format Changed in version 3.1: The positional argument specifiers can be omitted for str.format()
    print("str.format with {}{}".format(str_one_argument, " or two..."))

    # template
    str_template = Template("I have a template with $what")
    print(str_template.substitute(what=str_one_argument))


def string_formatting_types_based_on_placeholders():
    print(f"This is a {'left':<10} align.")
    print(f"This is a {'right':>10} align.")
    print(f"This is a {'center':^10} align.")
    print(f"10 in binary is {10:b}")
    print(f"0.55 is {0.55:.0%}")  # Percentage format
    print(f"I want {1000000:,}USD")  # Use comma as a thousand separator


def split():
    lorem_ipsum = "Lorem ipsum dolor sit amet"
    splitted_string = lorem_ipsum.split()  # To split on whitespace don’t have to give split any arguments

    print("String splitting:")
    print(f"\tsplitted string: {splitted_string}")


def join():
    lorem_ipsum = ["lorem", "ipsum", "dolor", "sit", "amet"]
    joined_string = " ".join(lorem_ipsum)

    print("String joining:")
    print(f"\tjoined string: {joined_string}")


def reverse():
    # noinspection SpellCheckingInspection
    s = "ytrewq"
    reversed_s = s[::-1]  # slicing

    print(f"Reversing: {s} backwards is {reversed_s}")


if __name__ == '__main__':
    multiline_strings()
    capitalize()
    number_formatting()
    string_formatting()
    string_formatting_types_based_on_placeholders()
    split()
    join()
    reverse()
