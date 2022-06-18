#!/usr/bin/python3

# Python does not support overloading
# So if you want to overload a function this is the way
def function(optional_argument=True):
    if optional_argument is True:
        print("Ok, it's true")
    else:
        print("It's false")


if __name__ == '__main__':
    function()
    function(False)
