#!/usr/bin/env python3

KEY = b'123456'
PLAINTEXT = b'hello world!'


# noinspection PyShadowingNames
def _xor(key: bytes, stream: bytes) -> bytes:
    xored_stream = b''
    stream_length = len(stream)
    key_length = len(key)

    # We assume that key_length <= stream_length
    for i in range(stream_length):
        xored_stream += bytes([stream[i] ^ key[i % key_length]])

    return xored_stream


if __name__ == '__main__':
    ciphertext = _xor(KEY, PLAINTEXT)  # key ⊕ plaintext = ciphertext
    decrypted_text = _xor(KEY, ciphertext)  # key ⊕ ciphertext = plaintext

    print(f"Plaintext: '{PLAINTEXT.decode()}'")
    # return: Plaintext: 'hello world!'

    print(f"Ciphertext: '{ciphertext.decode()}'")
    # return: Ciphertext: 'YW_XZF]AXQ'

    print(f"Decrypted text: '{decrypted_text.decode()}'")
    # return: Decrypted text: 'hello world!'
