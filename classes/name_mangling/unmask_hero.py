#!/usr/bin/env python3

from classes.name_mangling.Hero import Hero

if __name__ == '__main__':
    batman: Hero = Hero('Batman', 'Bruce Wayne')

    batman.print_name()
    # return: I'm Batman!

    # noinspection PyProtectedMember
    batman._print_real_name()  # Access to a protected member method
    # return: PWNED! I'm Bruce Wayne :(

    # noinspection PyUnresolvedReferences,PyProtectedMember
    print(batman._Hero__real_name)  # Access to a protected (name mangled) attribute
