#!/usr/bin/env python3

# # Constant value pattern.
# Like the literal patterns but for certain named constants.
# It must be a qualified (dotted) name.
# Only matches values equal to the corresponding value.
# It never binds.

from enum import Enum


class Informational(Enum):
    CONTINUE = 'https://http.cat/status/100'
    SWITCHING_PROTOCOLS = 'https://http.cat/status/101'
    PROCESSING = 'https://http.cat/status/102'
    EARLY_HINTS = 'https://http.cat/status/103'


def _get_status(code: Informational) -> str:
    match code:
        case Informational.CONTINUE:
            return f"Ok, {Informational.CONTINUE.value}"
        case _:
            return 'Something\'s wrong. No cats for you.'


if __name__ == '__main__':
    print(_get_status(Informational.CONTINUE))
    # return: Ok, https://http.cat/status/100
