#!/usr/bin/env python3

import hashlib

_TEXT = 'Hello world!'

if __name__ == '__main__':
    hash_object = hashlib.sha256(_TEXT.encode())
    hash_digest = hash_object.hexdigest()

    print(f"SHA256 hash of '{_TEXT}' is '{hash_digest}'")
    # return: SHA256 hash of 'Hello world!' is 'c0535e4be2b79ffd93291305436bf889314e4a3faec05ecffcbb7df31ad9e51a'

