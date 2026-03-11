#!/usr/bin/env python3

"""
Since version 3.7, Python offers data classes.

Advantages:
   * Requires a minimal amount of code
   * Automatically generated magic methods:
       * __init__
       * __eq__
       * __repr__
       * __hash__
   * Requires type hints (reduces the chances of bugs)
   * You can create immutable dataclasses by setting frozen=True
"""

from dataclasses import dataclass

if __name__ == "__main__":

    @dataclass
    class Fighter:
        name: str
        suit: str

    fighter1 = Fighter("Ryu", "black")
    fighter2 = Fighter("Ryu", "black")

    print(fighter1 == fighter2)
    # return: True

    print(fighter1.name)
    # return: Ryu

    print(fighter1)
    # return: Fighter(name='Ryu', suit='black')
