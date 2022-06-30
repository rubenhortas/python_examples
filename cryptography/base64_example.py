#!/usr/bin/env python3

import base64

MESSAGE = "Hello world!"

if __name__ == '__main__':
    print(f"message: {MESSAGE}")

    # Encode
    message_bytes = MESSAGE.encode('ascii')
    base64_message = base64.b64encode(message_bytes).decode()  # .decode() to convert from bytes to string
    print(f"base64_message: {base64_message}")

    # Decode
    decoded_message = base64.b64decode(base64_message).decode()   # .decode() to convert from bytes to string
    print(f"decoded_message: {decoded_message}")
