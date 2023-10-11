#!/usr/bin/env python3

import base64

MESSAGE = "Hello world!"

if __name__ == '__main__':
    print(f"message: {MESSAGE}")
    # return: message: Hello world!

    # Encode to base64
    message_bytes = MESSAGE.encode()
    base64_message = base64.b64encode(message_bytes).decode()  # convert from bytes to string
    print(f"base64_message: {base64_message}")
    # return: base64_message: SGVsbG8gd29ybGQh

    # Decode from base64
    decoded_message = base64.b64decode(base64_message).decode()  # convert from bytes to string
    print(f"decoded_message: {decoded_message}")
    # return: decoded_message: Hello world!
