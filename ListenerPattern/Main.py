#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:        Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:       rubenhortas at gmail.com
@github:        http://github.com/rubenhortas
@license:       CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:          Main.py
@interpreter:   2.7
"""

"""
Example of Listener Pattern implementation.
"""
from IListener import IListener
from ListenerClass import ListenerClass
from Subject import Subject


if __name__ == "__main__":
    print("main")
    subject = Subject(ListenerClass())