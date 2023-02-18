#!/usr/bin/env python3

def _xor(key: bytes, stream: bytes) -> bytes:
    xord_stream = b''
    stream_length = len(stream)
    key_length = len(key)

    # We assume that key_length <= stream_length
    for i in range(stream_length):
        xord_stream += bytes([stream[i] ^ key[i % key_length]])

    return xord_stream


if __name__ == '__main__':
    key = b'123456'
    plaintext = b'hello world!'

    ciphertext = _xor(key, plaintext)
    decrypted_text = _xor(key, ciphertext)

    print(f"Plaintext: '{plaintext.decode()}'")
    print(f"Ciphertext: '{ciphertext.decode()}'")
    print(f"Decrypted text: '{decrypted_text.decode()}'")
