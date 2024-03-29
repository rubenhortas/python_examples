#!/usr/bin/env python3

# A class pattern provides support for destructuring arbitrary objects.
# There are two possible ways of matching on object attributes: by position like Point(1, 2), and by name like Point(x=1, y=2).
# These two can be combined, but a positional match cannot follow a match by name.
# Each item in a class pattern can be an arbitrary pattern.
# Whether a match succeeds or not is determined by the equivalent of an isinstance call.
# If the subject is not an instance of the named class, the match fails.

class Cat:
    url = None

    def __init__(self, code):
        self.url = f"https://http.cat/status/{code}"


class Dog:
    url = None

    def __init__(self, code):
        self.url = f"https://httpstatusdogs.com/{code}"


def _get_pet(pet: Cat | Dog) -> None:
    match pet:
        case Cat():
            print(f"Cat url: {pet.url}")
        case Dog():
            print('I don\'t want to print dog urls :(')


if __name__ == '__main__':
    _get_pet(Cat(200))
    # return: Cat url: https://http.cat/status/200

    _get_pet(Dog(404))
    # return: I don't want to print dog urls :(
