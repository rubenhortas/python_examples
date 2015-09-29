#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      ListenerClass.py
"""

from IListener import IListener

class ListenerClass(IListener):
            
    def notify(self, msg):
        print("I'm a listener and have a new message: {0}".format(msg))