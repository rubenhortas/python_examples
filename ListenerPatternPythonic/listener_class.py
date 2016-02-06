#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        ListenerClass.py
@interpreter: python3
"""


class ListenerClass:

    @staticmethod
    def notify(msg):
        print("I'm a listener and have a new message: {0}".format(msg))
