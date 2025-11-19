#!/usr/bin/env python3

import hashlib

_FILE = 'helloworld.txt'
_CHUNK_SIZE = 65536  # 64KB

def _hash_file(file_path: str) -> str:
    h = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(_CHUNK_SIZE)

            if chunk == b'':
                break

            h.update(chunk)

    return h.hexdigest()


if __name__ == '__main__':
    print(f"SHA256 hash of '{_FILE}' is '{_hash_file(_FILE)}'")
    # return: SHA256 hash of 'helloworld.txt' is '871cf6acfafad3ccb5cd583916451dee354b2e4fa2cccb2205d0398ce79d5f80'
