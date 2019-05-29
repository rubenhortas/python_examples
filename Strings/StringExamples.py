#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:        Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:       rubenhortas at gmail.com
@github:        http://github.com/rubenhortas
@license:       CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:          StringExamples.py
@interpreter:   python 2.7
"""

if __name__ == '__main__':

    # Triple quotes allow printing in several lines with a single instruction
    print("""Hello
    world""")
    print

    print('''Hello
    world''')
    print

    # Return a copy of the string with only its first character capitalized
    str = "hello world"
    print(str.capitalize())
    print

    # Format examples
    print("I have %d cats" % 2)
    print("I have %3d cats" % 2)
    print("I have %03d cats" % 2)
    print("I have %f cats" % 2)
    print("I have %.2f cats" % 2)
    print