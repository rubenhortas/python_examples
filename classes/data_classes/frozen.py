#!/usr/bin/env python3

from dataclasses import FrozenInstanceError, dataclass


@dataclass(frozen=True)  # frozen=True makes instances of the class immutable
class _Car:
    make: str
    model: str

    def __str__(self) -> str:
        return f"{self.make} {self.model}"


if __name__ == "__main__":
    daily = _Car("opel", "astra")
    sporty = _Car("suzuki", "swift sport")

    try:
        daily.make = "Kia"
        daily.make = "Niro"
    except FrozenInstanceError:
        print("You can't switch cars!")

    # return: You can't switch cars!
