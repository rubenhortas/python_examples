#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        default_arguments.py
@interpreter: python3
"""


def function(optionalArgument=True):
    if optionalArgument is True:
        print("Ok, it's true")
    else:
        print("It's false")


if __name__ == "__main__":
    function()
    function(False)
