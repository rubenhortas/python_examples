#!/usr/bin/env python3

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

_PLAINTEXT = 'Hello, RSA!'
_PUBLIC_EXPONENT = 65537
_KEY_SIZE = 2048
_ENCODING = 'UTF-8'


# noinspection PyShadowingNames
def encrypt(public_key: RSAPublicKey, oaep_padding: padding.OAEP, plaintext: str) -> bytes:
    return public_key.encrypt(plaintext.encode(_ENCODING), oaep_padding)

# noinspection PyShadowingNames
def decrypt(private_key: RSAPrivateKey, oaep_padding: padding.OAEP, ciphertext: bytes) -> str:
    return private_key.decrypt(ciphertext, oaep_padding).decode(_ENCODING)

if __name__ == '__main__':
    private_key = rsa.generate_private_key(public_exponent=_PUBLIC_EXPONENT, key_size=_KEY_SIZE)
    public_key = private_key.public_key()
    oaep_padding = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),label=None)
    ciphertext = encrypt(public_key, oaep_padding, _PLAINTEXT)
    decrypted_text = decrypt(private_key, oaep_padding, ciphertext)

    print(f"Plaintext: '{_PLAINTEXT}'")
    print(f"Ciphertext: '{ciphertext.hex()}'")
    print(f"Decrypted_plaintext: '{decrypted_text}'")
    # return:
    # Plaintext: 'Hello, RSA!'
    # Ciphertext: '7f44a13ae5c601fe9e1deb28fec4c45052ed15126ed3ec637810bdb9aaef0cddc024305409cca95f2f9127880eb5a11cc6c6df8d3bd945304296453d2e0bbe2581b87291cd3c68311aab0ca1ee8727039067164f4cf976c54f62026996b02260c3196987432288c4b89dd2d55d68852fb13df65aab91a285a71575b2217a2c7389d419eac080c8ddd6b56531066ac88c63ea3575d5d4d520850a9ba454e300ffce924c114fb3fd790aea59ca1b300828dc757bebff51492a23caec867c11bb4f926793fe58d3b6934a6cc0c42f1b31cf1566ce7632f2c147f0673444250734a5ec76d2234895b900b092157cee6616da960dc1574ca3bc6af03aab726ff9f7b7'
    # Decrypted_plaintext: 'Hello, RSA!'
