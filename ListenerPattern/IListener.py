#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      IListener.py
"""

"""
In python there is no such thing as interface, but this is an ilustrative 
example
"""
from abc import ABCMeta, abstractmethod


class IListener(metaclass=ABCMeta):

    def notify(self, msg):
        raise NotImplementedError