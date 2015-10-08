#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      Subject.py
"""


class Subject:
    listener = None
    notify_message = "Good news everyone!"

    def __init__(self, listener):

        self.listener = listener

        print("I'm a subject")
        print("I have a listener: ", self.listener)
        print("I'll notify my listener")

        self.listener.notify(notify_message)
