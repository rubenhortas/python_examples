#!/usr/bin/env python3

KEY = b'123456'
PLAINTEXT_STRING = b'hello world!'


def _xor(key: bytes, data: bytes) -> bytes:
    xored_data = b''

    for i in range(len(data)):
        xored_data += bytes([data[i] ^ key[i % len(key)]])
    return xored_data


if __name__ == '__main__':
    xored_data = _xor(KEY, PLAINTEXT_STRING)
    unxored_data = _xor(KEY, xored_data)

    print('Plaintext string: "' + PLAINTEXT_STRING.decode() + '"')
    print('Xored string: "' + xored_data.decode() + '"')
    print('Unxored string: "' + unxored_data.decode() + '"')
