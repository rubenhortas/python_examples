"""
__slots__ reduces the memory footprint of instances.
Instead of a dynamic dictionary to store attributes, Python uses a more compact structure.

Benefits of Using __slots__
    * Memory efficiency
    * Faster attribute access
    * Preventing attribute creation
    * Improved performance in large classes
"""


class Hero:
    __slots__ = ["hero_name", "name"]

    def __init__(self, name: str, hero_name: str) -> None:
        self.name = name
        self.hero_name = hero_name

    def __str__(self) -> str:
        return f"Hero(name={self.name}, hero_name={self.hero_name})"
