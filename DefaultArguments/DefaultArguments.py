#!/usr/bin/env python3
# _*_ coding:utf-8 _*

def function(optional_argument=True):
    if optional_argument is True:
        print("Ok, it's true")
    else:
        print("It's false")


if __name__ == "__main__":
    function()
    function(False)