#!/usr/bin/env python3

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
    key = b'123456'
    plaintext = b'hello world!'

    ciphertext = _xor(key, plaintext)  # key ⊕ plaintext = ciphertext
    decrypted_text = _xor(key, ciphertext)  # ciphertext ⊕ key = plaintext

    print(f"Plaintext: '{plaintext.decode()}'")
    # return: Plaintext: 'hello world!'

    print(f"Ciphertext: '{ciphertext.decode()}'")
    # return: Ciphertext: 'YW_XZF]AXQ'

    print(f"Decrypted text: '{decrypted_text.decode()}'")
    # return: Decrypted text: 'hello world!'
