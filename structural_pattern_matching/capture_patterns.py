#!/usr/bin/env python3

def _get_cat(code: int) -> None:
    # A capture pattern serves as an assignment target for the matched expression.
    # Only a single name is allowed.
    # A capture pattern always succeeds.
    # A capture pattern appearing in a scope makes the name local to that scope.
    match code:
        case '':
            print('No cat :(')
        case code_:
            print(f"Your cat is https://http.cat/status/{code_}")


if __name__ == '__main__':
    _get_cat(500)
    # return: Your cat is https://http.cat/status/500
