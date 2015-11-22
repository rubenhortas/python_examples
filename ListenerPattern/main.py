#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:        Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:       rubenhortas at gmail.com
@github:        http://github.com/rubenhortas
@license:       CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:          main.py
@interpreter:   3
"""

"""
Example of Listener Pattern implementation.
"""
from iListener import IListener
from listener_class import ListenerClass
from subject import Subject


if __name__ == "__main__":
    print("main")
    subject = Subject(ListenerClass())