#!/usr/bin/env python3

# Python does not support overloading, so if you want to overload a function this is the way.
def _function(optional_argument: bool = True) -> None:
    if optional_argument is True:
        print("Ok, it's true")
    else:
        print("It's false")


if __name__ == '__main__':
    _function()
    # return: Ok, it's true

    _function(False)
    # return: It's false
