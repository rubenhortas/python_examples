#!/usr/bin/env python3
# _*_ coding:utf-8 _*

import base64


if __name__ == '__main__':

    message = "Hello world!"
    print("message: %s" % message)

    # Encode
    message_bytes = message.encode('ascii')
    base64_message = base64.b64encode(message_bytes)
    print("base64_message: %s" % base64_message)

    # Decode
    decoded_message = base64.b64decode(base64_message)
    print("decoded_message: %s" % decoded_message)



