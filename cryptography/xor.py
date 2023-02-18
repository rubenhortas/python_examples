#!/usr/bin/env python3

def _xor(key: bytes, stream: bytes) -> bytes:
    xord_stream = b''

    # We assume that the len(key) <= len(stream)
    for i in range(len(stream)):
        xord_stream += bytes([stream[i] ^ key[i % len(key)]])
    return xord_stream


if __name__ == '__main__':
    key = b'123456'
    plaintext = b'hello world!'

    ciphertext = _xor(key, plaintext)
    decrypted_text = _xor(key, ciphertext)

    print(f"Plaintext: '{plaintext.decode()}'")
    print(f"Ciphertext: '{ciphertext.decode()}'")
    print(f"Decrypted text: '{decrypted_text.decode()}'")
