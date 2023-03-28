#!/usr/bin/env python3

from dataclasses import dataclass

# Since version 3.7, Python offers data classes.
# Advantages:
#    - requires a minimal amount of code
#    - __eq__ is implemented
#    - __repr__ is implemented (for print)
#    - requires type hints (reduces the chances of bugs)
if __name__ == '__main__':

    @dataclass
    class Fighter:
        name: str
        suit: str

    fighter = Fighter("Ryu", "black")

    print(fighter == fighter)  # True
    print(fighter.name)  # Ryu
    print(fighter)  # Fighter(name='Ryu', suit='black')
