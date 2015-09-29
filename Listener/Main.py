#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      Main.py
"""

from Subject import Subject
from ListenerClass import ListenerClass
from IListener import IListener

"""
Example of Listener Pattern implementation.
"""
if __name__ == "__main__":
    print("main")
    subject = Subject(ListenerClass())