#!/usr/bin/env python3

from dataclasses import dataclass

"""
__slots__ reduces the memory footprint of instances.
Instead of a dynamic dictionary to store attributes, Python uses a more compact structure.

Benefits of Using __slots__
    * Memory efficiency
    * Faster attribute access
    * Preventing attribute creation
    * Improved performance in large classes
"""


# The 'slots=True' parameter (introduced in Python 3.10) automatically defines __slots__ based on the dataclass fields.
@dataclass(slots=True)
class _Hero:
    # Example of manual __slots__ for older Python versions (< 3.10)
    # __slots__ = ["hero_name", "name"]
    hero_name: str
    name: str

    def __str__(self) -> str:
        return f"_Hero(name={self.name}, hero_name={self.hero_name})"


if __name__ == "__main__":
    hero = _Hero("Robbie Reyes", "Ghost Rider")
    print(f"I'm {hero.name}, and I'm {hero.hero_name}")
