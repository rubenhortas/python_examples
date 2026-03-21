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


@dataclass
class _Fighter:
    name: str
    suit: str


if __name__ == "__main__":
    fighter1 = _Fighter("Ryu", "black")
    fighter2 = _Fighter("Ryu", "black")

    print(fighter1 == fighter2)
    # return: True

    print(fighter1.name)
    # return: Ryu

    print(fighter1)
    # return: _Fighter(name='Ryu', suit='black')
