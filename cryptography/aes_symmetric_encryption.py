#!/usr/bin/env python3

import secrets

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

_PLAIN_TEXT = 'Hello, AES!'
_KEY_SIZE = 32  # bytes
_NONCE_SIZE = 12  # bytes
_ENCODING = 'UTF-8'

def encrypt(aes: AESGCM, nonce: bytes, plaintext: str) -> str:
    return (nonce + aes.encrypt(nonce, plaintext.encode(_ENCODING), None)).hex()

def decrypt(aes: AESGCM, ciphertext: str) -> str:
    ciphertext_bytes = bytes.fromhex(ciphertext)
    nonce = ciphertext_bytes[:_NONCE_SIZE]
    encrypted_data = ciphertext_bytes[_NONCE_SIZE:]

    return aes.decrypt(nonce, encrypted_data, None).decode(_ENCODING)

if __name__ == '__main__':
    key = secrets.token_bytes(_KEY_SIZE)
    nonce = secrets.token_bytes(_NONCE_SIZE)  # A number that is unsed only once
    aes = AESGCM(key)
    ciphertext = encrypt(aes, nonce, _PLAIN_TEXT)
    decoded_ciphertext = decrypt(aes, ciphertext)

    print(f"Plaintext: {_PLAIN_TEXT}'")
    print(f"Key: '{key.hex()}'")
    print(f"Ciphertext: '{ciphertext}'")
    print(f"Decrypted text: '{decoded_ciphertext}'")
    #return:
    # Plaintext: Hello, AES!'
    # Key: '450d0b49bfc86b8180c437d7b6e711f84dc96e72d28cff06318bc0919ee7189c'
    # Ciphertext: 'afa250e2e4aecdb9104a5b1eecf97e329168111bf708f2d9b8ce30a6908825370074be525c834e'
    # Decrypted text: 'Hello, AES!'
