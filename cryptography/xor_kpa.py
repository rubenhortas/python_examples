#!/usr/bin/env python3

import os

KEY_LENGTH = 4


# noinspection PyShadowingNames
def __initialize():
    print("Initializing values...")

    plain_text_string = "Hello world!".encode()  # string to bytes
    xor_key = os.urandom(KEY_LENGTH)  # Random KEY_LENGTH bytes KEY
    xor_string = __xor(xor_key, plain_text_string)

    print(f"\tplain_text_string: {plain_text_string.decode()}")
    print(f"\txor_key: {xor_key}")
    print(f"\tciphertext: {xor_string}")
    print()

    return plain_text_string, xor_key, xor_string


# noinspection PyShadowingNames
def __xor(key: bytes, data: bytes) -> bytes:
    xored_data = b''

    for i in range(len(data)):
        xored_data += bytes([data[i] ^ key[i % len(key)]])
    return xored_data


# noinspection PyShadowingNames
def __get_xor_key(data: bytes, cipher_data: bytes) -> bytes:
    key = b''

    print("Guessing the secret KEY using for xor...")

    for i in range(KEY_LENGTH):
        key += bytes([data[i] ^ cipher_data[i]])

    print(f"\tGuessed KEY: {key}")
    print()

    return key


# Example of how it works and how to perform a Known-plaintext attack (KPA) on a xor ciphertext
if __name__ == '__main__':
    plain_text_string, key, ciphertext = __initialize()

    # If we have the initial plain text string (or at least a part) and the result ciphertext
    # we can guess the KEY used for cipher the string.
    guessed_key = __get_xor_key(plain_text_string, ciphertext)

    # If we have guessed the KEY we can guess the initial string
    guessed_plain_text_string = __xor(guessed_key, ciphertext)
    
    # Check the results
    print("Results:")
    print("\tKeys:")
    print(f"\t\tRandom generated KEY: {key}")
    print(f"\t\tGuessed KEY: {guessed_key}")
    print(("\t\tKeys are different", "\t\tKeys are equals")[key == guessed_key])  # keys are equal
    print()
    print("Initial strings:")
    print(f"\t\tInitial plain text string: {plain_text_string.decode()}")
    print(f"\t\tGuessed initial plain text string: {guessed_plain_text_string.decode()}")
    print(("\t\tStrings are different", "\t\tStrings are equals")[plain_text_string == guessed_plain_text_string])  # strings are equal
