#!/usr/bin/env python3

"""
Vigenere decrypter script

Based on the method explained by @Theoretically in https://www.youtube.com/watch?v=LaWp_Kq0cKs

Developed to solve levels 4 and 5 of the Krypton game on OverTheWire.
You can read my post here: https://rubenhortas.github.io/posts/overthewire-krytpon-levels-4-and-5-vigenere-cipher/

OverTheWire: https://overthewire.org/
Krypton Level 4: https://overthewire.org/wargames/krypton/krypton4.html
Krypton Level 5: https://overthewire.org/wargames/krypton/krypton5.html
"""

import argparse

from numpy import median

# English frequencies from: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# Alphabetically ordered!
LANGUAGE_FREQUENCIES = {
    'A': 8.4966,
    'B': 2.0720,
    'C': 4.5388,
    'D': 3.3844,
    'E': 11.1607,
    'F': 1.8121,
    'G': 2.4705,
    'H': 3.0034,
    'I': 7.5448,
    'J': 0.1965,
    'K': 1.1016,
    'L': 5.4893,
    'M': 3.0129,
    'N': 6.6544,
    'O': 7.1635,
    'P': 3.1671,
    'Q': 0.1962,
    'R': 7.5809,
    'S': 5.7351,
    'T': 6.9509,
    'U': 3.6308,
    'V': 1.0074,
    'W': 1.2899,
    'X': 0.2902,
    'Y': 1.7779,
    'Z': 0.2722
}


# noinspection PyShadowingNames
def _read_file(encrypted_file: str) -> str:
    ciphertext = ''

    with open(encrypted_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        for character in line:
            if _is_alphabetic(character):
                ciphertext = ciphertext + character.upper()

    return ciphertext


def _is_alphabetic(character: chr) -> bool:
    return ('a' <= character <= 'z') or ('A' <= character <= 'Z')


# noinspection PyShadowingNames
def _get_key_shifts(cipher_text: str, key_length: int) -> list:
    shifts = []
    language_frequency_values = _get_frequency_values(LANGUAGE_FREQUENCIES)

    for i in range(key_length):
        ciphertext_chars = cipher_text[i::key_length]
        ciphertext_chars_frequencies = _get_frequencies(ciphertext_chars)
        ciphertext_chars_complete_frequencies = _complete_frequencies(ciphertext_chars_frequencies)
        ciphertext_chars_frequency_values = _get_frequency_values(ciphertext_chars_complete_frequencies)

        shift = _get_key_shift(language_frequency_values, ciphertext_chars_frequency_values)
        shifts.append(shift)

    return shifts


def _get_frequency_values(character_frequencies: dict) -> list:
    frequency_values = []

    for character_frequency in character_frequencies:
        frequency_values.append(character_frequencies[character_frequency])

    return frequency_values


def _get_frequencies(characters: str) -> dict:
    characters_length = len(characters)
    frequencies = {}

    for i in characters:
        if i not in frequencies:
            frequencies[i] = ((characters.count(i) * 100) / characters_length)

    return frequencies


def _get_key_shift(language_frequency_values: list, ciphertext_frequency_values: list) -> int:
    """
    Finding numbers
    Multiply the frequencies of the alphabet (in order) by rotations of the frequencies of the cipher characters
    until the greatest sum is found. The largest sum will indicate the number of rotations or "shift".

    :param language_frequency_values: Frequency values of the language.
    :param ciphertext_frequency_values: Frequency values of the ciphertext.
    :return: Number of rotations or "shift".
    """
    alphabet_length = len(LANGUAGE_FREQUENCIES)
    shift = 0
    max_sum = 0

    for i in range(alphabet_length):
        ciphertext_frequency_sum = 0

        for j in range(alphabet_length):
            m = (i + j) % alphabet_length  # mod, used for rotation
            ciphertext_frequency_sum = ciphertext_frequency_sum + (
                    language_frequency_values[j] * ciphertext_frequency_values[m])

        if ciphertext_frequency_sum > max_sum:
            max_sum = ciphertext_frequency_sum
            shift = i

    return shift


# noinspection PyShadowingNames
def _get_key(shifts: list) -> str:
    key = ''

    for shift in shifts:
        i = 0

        for character in LANGUAGE_FREQUENCIES:
            if i == shift:
                key = key + character
                break

            i = i + 1

    return key


# noinspection PyShadowingNames
def _decrypt(ciphertext: str, ciphertext_length: int, key_shifts: list, key_length: int) -> str:
    alphabet = _get_alphabet()
    plaintext = ''

    for i in range(ciphertext_length):
        m = i % key_length
        plaintext = plaintext + alphabet[(alphabet.index(ciphertext[i]) - key_shifts[m]) % len(alphabet)]

    return plaintext


def _complete_frequencies(frequencies: dict) -> dict:
    complete_frequencies = {}

    for character_frequency in LANGUAGE_FREQUENCIES:
        if character_frequency in frequencies:
            complete_frequencies[character_frequency] = frequencies[character_frequency]
        else:
            complete_frequencies[character_frequency] = 0

    return complete_frequencies


def _get_alphabet() -> list:
    alphabet = []

    for character_frequency in LANGUAGE_FREQUENCIES:
        alphabet.append(character_frequency)

    return alphabet


# noinspection PyShadowingNames
def _get_shifts_from_key(key: str) -> list:
    shifts = []

    for key_character in key:
        i = 0

        for character_frequency in LANGUAGE_FREQUENCIES:
            if key_character == character_frequency:
                shifts.append(i)
                break

            i = i + 1

    return shifts


# noinspection PyShadowingNames
def _get_key_length(ciphertext: str, ciphertext_length: int) -> int:
    coincidences = _get_coincidences(ciphertext, ciphertext_length)

    return _get_max_coincidences(coincidences)


# noinspection PyShadowingNames
def _get_coincidences(ciphertext: str, ciphertext_length: int) -> list:
    """
    Finding coincidences
    Rotate the ciphertext from 1 to n positions to the right and count the character matches with the original ciphertext by position.
    For instance:
       CT: ABCABCABC
    RCT 1:  ABCABCAB Coincidences = 0
    RCT 2:   ABCABCA Coincidences = 0
    RCT 3:    ABCABC Coincidences = 6

    :param ciphertext: Ciphertext.
    :param ciphertext_length: Ciphertext_length.
    :return: List with the number of coincidences for each rotation.
    """
    max_length = ciphertext_length - 1
    coincidences = []

    for i in range(max_length):
        comparison_chars = ciphertext[:(max_length - i)]  # Rotated ciphertext
        comparison_chars_length = len(comparison_chars)
        coincidences_sum = 0

        for j in range(comparison_chars_length):
            if ciphertext[j + i + 1] == comparison_chars[j]:
                coincidences_sum = coincidences_sum + 1

        coincidences.append(coincidences_sum)

    return coincidences


# noinspection PyShadowingNames
def _get_max_coincidences(coincidences: list) -> int:
    """
    Find the position in the list with the largest match values.
    The position will be the key length.

    :param coincidences: Number of coincidences.
    :return: The position in the list with the largest match values.
    """
    key_length = 0
    coincidences_length = len(coincidences)
    max_median = 0

    for i in range(coincidences_length):
        list_slice = coincidences[i::i + 1]

        # len(lst) < key length = i + 1 (The key length cannot be greater than the list slice)
        if len(list_slice) >= (i + 1):
            if median(list_slice) > max_median:
                max_median = median(list_slice)
                key_length = i + 1

    return key_length


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vigenere Decrypter')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-k', '--key', dest='key', nargs=1, help='decrypt key')
    group.add_argument('-kl', '--key-length', dest='key_length', nargs=1, help='decrypt key length')
    parser.add_argument('encrypted_file', nargs=1, help='encrypted file')

    args = parser.parse_args()

    key_length = 0
    key_shifts = []
    key = ''
    pt = ''
    ciphertext = _read_file(args.encrypted_file[0])
    ciphertext_length = len(ciphertext)

    if args.key is None and args.key_length is None:
        key_length = _get_key_length(ciphertext, ciphertext_length)
        key_shifts = _get_key_shifts(ciphertext, key_length)
        key = _get_key(key_shifts)

    if args.key_length is not None:
        key_length = int(args.key_length[0])
        key_shifts = _get_key_shifts(ciphertext, key_length)
        key = _get_key(key_shifts)

    if args.key is not None:
        key = args.key[0].upper()
        key_length = len(key)
        key_shifts = _get_shifts_from_key(key)

    if key_length > 0:
        pt = _decrypt(ciphertext, ciphertext_length, key_shifts, key_length)

        print(f"key: {key}\n")
        print(f"ct: {ciphertext}\n")
        print(f"pt: {pt}\n")
    else:
        print(f"Key length = 0.")
