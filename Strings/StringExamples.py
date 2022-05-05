#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

if __name__ == '__main__':

    # Triple quotes allow printing in several lines with a single instruction
    print("""Hello
    world""")
    print()

    print('''Hello
    world''')
    print()

    # Return a copy of the string with only its first character capitalized
    s = "hello world"
    print(s.capitalize())
    print()

    # Format examples
    print("I have %d cats" % 2)
    print("I have %3d cats" % 2)
    print("I have %03d cats" % 2)
    print("I have %f cats" % 2)
    print("I have %.2f cats" % 2)
    print()