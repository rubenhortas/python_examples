#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        fractionsExample.py
@interpreter: python3
"""

from fractions import Fraction


if __name__ == '__main__':
    x = Fraction(1, 5)  # Numerator, Denominator
    result = 3 * x
    print(result)
