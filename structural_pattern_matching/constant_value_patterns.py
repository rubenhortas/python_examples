#!/usr/bin/env python3

from enum import Enum


class Informational(Enum):
    CONTINUE = 'https://http.cat/status/100'
    SWITCHING_PROTOCOLS = 'https://http.cat/status/101'
    PROCESSING = 'https://http.cat/status/102'
    EARLY_HINTS = 'https://http.cat/status/103'


def _get_status(code: Informational) -> str:
    match code:
        # # Constant value pattern. like the literal but for certain named constants.
        # It must be a qualified (dotted) name.
        # Only matches values equal to the corresponding value.
        # It never binds.
        case Informational.CONTINUE:
            return f"Ok, {Informational.CONTINUE}"
        case _:
            return 'Something\'s wrong. No cats for you.'


if __name__ == '__main__':
    print(_get_status(Informational.CONTINUE))
    # return: Ok, Informational.CONTINUE
