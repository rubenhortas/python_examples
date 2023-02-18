#!/usr/bin/env python3

import os

KEY_LENGTH = 4


# noinspection PyShadowingNames
def _initialize():
    print("Initializing values...")

    plaintext = "Hello world!".encode()  # string to bytes
    key = os.urandom(KEY_LENGTH)  # Random KEY_LENGTH bytes KEY
    ciphertext = _xor(key, plaintext)

    print(f"\tplaintext: {plaintext.decode()}")
    print(f"\tkey: {key}")
    print(f"\tciphertext: {ciphertext}")
    print()

    return plaintext, key, ciphertext


# noinspection PyShadowingNames
def _xor(key: bytes, stream: bytes) -> bytes:
    xord_stream = b''
    stream_length = len(stream)
    key_length = len(key)

    # We assume that key_length <= stream_length
    for i in range(stream_length):
        xord_stream += bytes([stream[i] ^ key[i % key_length]])
    return xord_stream


# noinspection PyShadowingNames
def _get_xor_key(plaintext: bytes, ciphertext: bytes) -> bytes:
    key = b''

    print("Guessing the secret (random) KEY used for xor...")

    for i in range(KEY_LENGTH):
        key += bytes([plaintext[i] ^ ciphertext[i]])

    print(f"\tGuessed KEY: {key}")
    print()

    return key


# Example of how to perform a Known-plaintext attack (KPA) on a xor'd ciphertext
if __name__ == '__main__':
    plaintext, key, ciphertext = _initialize()

    # If we have the initial plain text string (or at least a part) and the result ciphertext
    # we can guess the KEY used for cipher the string.
    guessed_key = _get_xor_key(plaintext, ciphertext)

    # If we have guessed the KEY we can guess the initial string
    decrypted_text = _xor(guessed_key, ciphertext)

    # Check the results
    print("Results:")
    print("\tKeys:")
    print(f"\t\tRandom generated key: {key}")
    print(f"\t\tGuessed key: {guessed_key}")
    print(("\t\tKeys are different", "\t\tKeys are equals")[key == guessed_key])  # keys are equal
    print()
    print("Initial strings:")
    print(f"\t\tInitial plaintext: {plaintext.decode()}")
    print(f"\t\tDecrypted text: {decrypted_text.decode()}")
    print(("\t\tStrings are different", "\t\tStrings are equals")[plaintext == decrypted_text])  # strings are equal
