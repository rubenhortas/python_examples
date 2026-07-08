from collections.abc import Mapping
from types import MappingProxyType
from typing import ClassVar


class Rat:
    MOVES: ClassVar[Mapping[tuple[int, int], str]] = MappingProxyType(
        {
            (-1, 0): "U",  # Up
            (1, 0): "D",  # Down
            (0, 1): "R",  # Right
            (0, -1): "L",  # Left
        }
    )
