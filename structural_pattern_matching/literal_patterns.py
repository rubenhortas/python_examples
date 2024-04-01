#!/usr/bin/env python3

# Literal pattern types: number, string, 'True', 'False', None

def _get_http_status(code: int) -> str:
    match code:
        case None:
            return 'None'
        case True | False:
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
