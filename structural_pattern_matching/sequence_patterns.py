#!/usr/bin/env python3


def _get_match(collection):
    # A sequence pattern follows the same semantics as unpacking assignment.
    # Tuple-like and list-like syntax can be used, with identical semantics.
    # Each element can be an arbitrary pattern; there may also be at most one *name pattern to catch all remaining items.
    # To match a sequence pattern the subject must be an instance of collections.abc.Sequence, and it cannot be any kind of string (str, bytes, bytearray). It cannot be an iterator.
    # [*_] matches a sequence of any length.
    # (_, _, *_), matches any sequence of length two or more.
    # ["a", *_, "z"] matches any sequence of length two or more that starts with "a" and ends with "z".
    match collection:
        case 1, [collection, *others]:
            print('Got 1 and a nested sequence')
        case (1, x):
            print(f"Got 1 and {x}")


def _get_cat(action: list):
    match action:
        case ['get']:
            print('Which cat do you want?')
        case ['get', code]:
            print(f"https://http.cat/status/{code}")


if __name__ == '__main__':
    _get_match((1, 'asdf'))
    # return: Got 1 and asdf

    _get_match((1, [2, 3, 4]))
    # return: Got 1 and a nested sequence

    _get_cat(['get'])
    # return: Which cat do you want?

    _get_cat(['get', 500])
    # return: https://http.cat/status/500
