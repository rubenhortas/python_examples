#!/usr/bin/env python3

KEY = b'123456'
PLAINTEXT_STRING = b'hello world!'


def xor(key: bytes, data: bytes) -> bytes:
    xor_data = b''

    for i in range(len(data)):
        xor_data += bytes([data[i] ^ key[i % len(key)]])
    return xor_data


if __name__ == '__main__':
    xored_string = xor(KEY, PLAINTEXT_STRING)
    unxored_string = xor(KEY, xored_string)

    print('Plaintext string: "' + PLAINTEXT_STRING.decode() + '"')
    print('Xored string: "' + xored_string.decode() + '"')
    print('Unxored string: "' + unxored_string.decode() + '"')
