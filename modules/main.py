#!/usr/bin/env python3

from modules import module

if __name__ == '__main__':
    module.public_method()
    # return: Public method

    # In python nothing is really private
    # noinspection PyProtectedMember
    module._private_method()
    # return: Private method!
