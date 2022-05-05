#!/usr/bin/env python3
# _*_ coding:utf-8 _*

import base64


if __name__ == '__main__':

    message = "Hello world!"
    print("message: %s" % str(message))  # str(message) to remove b' from string output

    # Encode
    message_bytes = message.encode('ascii')
    base64_message = base64.b64encode(message_bytes).decode()  # .decode() to remove b' from string output
    print("base64_message: %s" % str(base64_message))

    # Decode
    decoded_message = base64.b64decode(base64_message).decode()  # .decode() to remove b' from string output
    print("decoded_message: %s" % decoded_message)



