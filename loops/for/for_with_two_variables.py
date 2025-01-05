#!/usr/bin/env python3
import itertools

NAMES = ['Philip', 'Hercule', 'Pepe']
SURNAMES = ['Marlowe', 'Poirot', 'Carvalho']

if __name__ == '__main__':
    # Simulate a nested loop
    for i, j in itertools.product(range(len(NAMES)), range(len(SURNAMES))):
        print(f"{NAMES[i]} {SURNAMES[j]}")
    # result:
    # Philip Marlowe
    # Philip Poirot
    # Philip Carvalho
    # Hercule Marlowe
    # Hercule Poirot
    # Hercule Carvalho
    # Pepe Marlowe
    # Pepe Poirot
    # Pepe Carvalho

    print()

    # Loop simultaneously
    for name, surname in zip(NAMES, SURNAMES):
        print(f"{name} {surname}")
    # result:
    # Philip Marlowe
    # Hercule Poirot
    # Pepe Carvalho
