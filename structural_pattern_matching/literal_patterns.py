#!/usr/bin/env python3

"""
https://peps.python.org/pep-0622/
Pattern matching statement to Python, inspired by similar syntax found in Scala, Erlang, and other languages.

A match statement compares a value (the subject) to several different shapes (the patterns) until a shape fits.

Syntactically, a match statement contains:
    - a subject expression
    - one or more case clauses

Each case clause specifies:
    - a pattern (the overall shape to be matched)
    - an optional “guard” (a condition to be checked if the pattern matches)
    - a code block to be executed if the case clause is selected
"""


def _get_http_status(code: int) -> str:
    # The match statement tries to match a single subject to each of the patterns in its case clauses.
    # At the first successful match to a pattern in a case clause the variables in the pattern are assigned, and a corresponding block is executed.
    # Each case clause can also specify an optional boolean condition, known as a guard.
    match code:  # The subject
        # The patterns
        # Each pattern describes the type and structure of the accepted values as well as the variables where to capture its contents.
        case None:  # Literal pattern: number, string, 'True', 'False', None
            return 'None'
        case True | False:  # Literal pattern: number, string, 'True', 'False', None
            return '{status}'
        case 400:
            return 'https://http.cat/status/400'
        case 404:
            return 'https://http.cat/status/404'
        case 418:
            return 'https://http.cat/status/418'
        case 401 | 403 | 404:  # OR pattern. It matches if any of its sub-patterns match. It uses the binding for the leftmost pattern that matched.
            return 'Not allowed and no cat :('
        case _:  # The wildcard pattern '_' always matches, but does not capture any variable.
            return 'Something\'s wrong. No cats for you.'


if __name__ == '__main__':
    print(_get_http_status(418))
    # return: https://http.cat/status/418
