#!/usr/bin/env python3

import hashlib
from pathlib import Path

_FILE = "helloworld.txt"


def _hash_file(file_path: Path, chunk_size: int = 65536) -> str:
    if not file_path.is_file():
        raise FileNotFoundError

    hasher = hashlib.sha256()

    with file_path.open("rb") as stream:
        # Use iter() with a callable and a sentinel (b'') to eliminate the explicit loop-and-break
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


if __name__ == "__main__":
    try:
        print(f"SHA256 hash of '{_FILE}' is '{_hash_file(Path(_FILE).resolve())}'")
    except FileNotFoundError:
        print(f"'{_FILE}' not found.")
    # return: SHA256 hash of 'helloworld.txt' is '871cf6acfafad3ccb5cd583916451dee354b2e4fa2cccb2205d0398ce79d5f80'
