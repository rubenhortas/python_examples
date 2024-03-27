#!/usr/bin/env python3

def _get_cat(code: int):
    # A capture pattern serves as an assignment target for the matched expression.
    # Only a single name is allowed.
    # A capture pattern always succeeds.
    # A capture pattern appearing in a scope makes the name local to that scope.
    match code:
        case '':
            print('No cat :(')
        case name:
            print(f"Your cat is https://http.cat/status/{code}")


if __name__ == '__main__':
    _get_cat(500)
