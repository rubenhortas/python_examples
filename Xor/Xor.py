#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import os

KEY_LENGTH = 4


def initialize():
    print("Initializing values...")
    plain_text_string = "Hello world!".encode("utf-8")  # to bytes
    print("\tplain_text_string: %s" % plain_text_string.decode("utf-8"))

    xor_key = os.urandom(KEY_LENGTH)  # Random KEY_LENGTH bytes key
    print("\txor_key: %s" % xor_key)

    xor_string = xor(xor_key, plain_text_string)
    print("\txor_string: %s" % xor_string)
    print()

    return plain_text_string, xor_key, xor_string


def xor(key: bytes, data: bytes) -> bytes:
    xor_data = b''

    for i in range(len(data)):
        xor_data += bytes([data[i] ^ key[i % len(key)]])
    return xor_data


def getXorKey(data: bytes, xor_data: bytes) -> bytes:
    key = b''

    print("Guessing the secret key using for xor...")

    for i in range(KEY_LENGTH):
        key += bytes([data[i] ^ xor_data[i]])

    print("\tGuessed key: %s" % key)
    print()

    return key


if __name__ == "__main__":
    plain_text_string, key, xor_string = initialize()

    # We can guess the key used for xor the string
    guessed_key = getXorKey(plain_text_string, xor_string)

    # Check the results
    guessed_plain_text_string = xor(guessed_key, xor_string)
    print("Results:")
    print("\tRandom generated key: %s" % key)
    print("\tGuessed key: %s" % guessed_key)
    print(("\tKeys are different", "\tKeys are equals")[key == guessed_key])  # keys are equal
    print("\tInitial plain text string: %s" % plain_text_string.decode("utf-8"))
    print("\tGuessed initial plain text string: %s" % guessed_plain_text_string.decode("utf-8"))
    print(("\tStrings are different", "\tStrings are equals")[plain_text_string == guessed_plain_text_string])  # strings are equal
