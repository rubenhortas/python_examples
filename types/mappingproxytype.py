#!/usr/bin/env python3


from types import MappingProxyType


class _ComicCollection:
    def __init__(self, **comics: str) -> None:
        self._comics = comics  # Internal dictionary to hold comic titles and their details
        self.comics = MappingProxyType(self._comics)  # Read-only view of comics

    def add_comic(self, title: str, details: str) -> None:
        self._comics[title] = details
        self.comics = MappingProxyType(self._comics)  # Update the read-only view


if __name__ == "__main__":
    collection = _ComicCollection(
        Spiderman="A superhero comic about Peter Parker.", Batman="A superhero comic featuring Bruce Wayne."
    )
    print(collection.comics)
    # return: {'Spiderman': 'A superhero comic about Peter Parker.', 'Batman': 'A superhero comic featuring Bruce Wayne.'}

    # Attempting to modify the read-only view will raise an error
    try:
        collection.comics["Spiderman"] = "Updated details."
    except TypeError:
        print("You can't update this collection.")
    # return: You can't update this collection.

    collection.add_comic("X-Men", "A comic about a team of mutant superheroes.")
    print(collection.comics)
    # return: {'Spiderman': 'A superhero comic about Peter Parker.', 'Batman': 'A superhero comic featuring Bruce Wayne.', 'X-Men': 'A comic about a team of mutant superheroes.'}

