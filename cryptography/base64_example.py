#!/usr/bin/env python3

import base64

PLAINTEXT = 'Hello world!'

if __name__ == '__main__':
    print(f"message: {PLAINTEXT}")
    # return: message: Hello world!

    # Encode to base64
    plaintext_bytes = PLAINTEXT.encode()
    base64_text = base64.b64encode(plaintext_bytes).decode()  # convert from bytes to string
    print(f"base64_text: {base64_text}")
    # return: base64_text: SGVsbG8gd29ybGQh

    # Decode from base64
    decoded_text = base64.b64decode(base64_text).decode()  # convert from bytes to string
    print(f"decoded_text: {decoded_text}")
    # return: decoded_text: Hello world!
