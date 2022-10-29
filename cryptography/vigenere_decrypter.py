#!/usr/bin/env python3
import argparse

from numpy import median

# Vigenere decrypter script
# Based on the method explained by @Theoretically in https://www.youtube.com/watch?v=LaWp_Kq0cKs
# Developed for solve levels 4 and 5 of the Krypton game on OverTheWire.
# OverTheWire: https://overthewire.org/
# Krypton Level 4: https://overthewire.org/wargames/krypton/krypton4.html
# Krypton Level 5: https://overthewire.org/wargames/krypton/krypton5.html

# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# English frequencies
# Alphabet in order!
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


def __read_file(encrypted_file):
    ciphertext = ''

    with open(encrypted_file, 'r') as f:
        encrypted_file_lines = f.readlines()

    for line in encrypted_file_lines:
        for character in line:
            if __is_alphabetic(character):
                ciphertext = ciphertext + character.upper()

    return ciphertext


def __is_alphabetic(character):
    return ('a' <= character <= 'z') or ('A' <= character <= 'Z')


def __get_key_shifts(cipher_text, key_length):
    shifts = []
    language_frequency_values = __get_frequency_values(LANGUAGE_FREQUENCIES)

    for i in range(key_length):
        ciphertext_chars = cipher_text[i::key_length]
        ciphertext_chars_frequencies = __get_frequencies(ciphertext_chars)
        ciphertext_chars_complete_frequencies = __complete_frequencies(ciphertext_chars_frequencies)
        ciphertext_chars_frequency_values = __get_frequency_values(ciphertext_chars_complete_frequencies)

        shift = __get_key_shift(language_frequency_values, ciphertext_chars_frequency_values)
        shifts.append(shift)

    return shifts


def __get_frequency_values(character_frequencies):
    frequency_values = []

    for character_frequency in character_frequencies:
        frequency_values.append(character_frequencies[character_frequency])

    return frequency_values


def __get_frequencies(characters):
    characters_length = len(characters)
    frequencies = {}

    for i in characters:
        if i not in frequencies:
            frequencies[i] = ((characters.count(i) * 100) / characters_length)

    return frequencies


# Finding numbers
# Multiply the frequencies of the alphabet (in order) by rotations of the frequencies of the cipher characters
# until the greatest sum is found. The largest sum will indicate the number of rotations or shift.
def __get_key_shift(language_frequency_values, ciphertext_frequency_values):
    alphabet_length = len(LANGUAGE_FREQUENCIES)
    shift = 0
    max_sum = 0

    for i in range(alphabet_length):
        ciphertext_frequency_sum = 0

        for j in range(alphabet_length):
            m = (i + j) % alphabet_length  # mod, used for rotation
            ciphertext_frequency_sum = ciphertext_frequency_sum + (language_frequency_values[j] * ciphertext_frequency_values[m])

        if ciphertext_frequency_sum > max_sum:
            max_sum = ciphertext_frequency_sum
            shift = i

    return shift


def __get_key(shifts):
    key = ''

    for shift in shifts:
        i = 0

        for character in LANGUAGE_FREQUENCIES:
            if i == shift:
                key = key + character
                break

            i = i + 1

    return key


def __decrypt(ciphertext, ciphertext_length, key_shifts, key_length):
    alphabet = __get_alphabet()
    plaintext = ''

    for i in range(ciphertext_length):
        m = i % key_length
        plaintext = plaintext + alphabet[(alphabet.index(ciphertext[i]) - key_shifts[m]) % len(alphabet)]

    return plaintext


def __complete_frequencies(frequencies):
    complete_frequencies = {}

    for character_frequency in LANGUAGE_FREQUENCIES:
        if character_frequency in frequencies:
            complete_frequencies[character_frequency] = frequencies[character_frequency]
        else:
            complete_frequencies[character_frequency] = 0

    return complete_frequencies


def __get_alphabet():
    alphabet = []

    for character_frequency in LANGUAGE_FREQUENCIES:
        alphabet.append(character_frequency)

    return alphabet


def __get_shifts_from_key(key):
    shifts = []

    for key_character in key:
        i = 0

        for character_frequency in LANGUAGE_FREQUENCIES:
            if key_character == character_frequency:
                shifts.append(i)
                break

            i = i + 1

    return shifts


def __get_key_length(ciphertext, ciphertext_length):
    coincidences = __get_coincidences(ciphertext, ciphertext_length)

    return __get_max_coincidences(coincidences)


# Finding coincidences
# Rotate the ciphertext from 1 to n positions to the right nd count the character matches with the original ciphertext by position.
# For instance:
#    CT: ABCABCABC
# RCT 1:  ABCABCAB Coincidences = 0
# RCT 2:   ABCABCA Coincidences = 0
# RCT 3:    ABCABC Coincidences = 6
def __get_coincidences(ciphertext, ciphertext_length):
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


# Find the position in the list with the largest match values.
# The position will be the key length.
def __get_max_coincidences(coincidences):
    key_length = 0
    coincidences_length = len(coincidences)
    max_median = 0

    for i in range(coincidences_length):
        list_slice = coincidences[i::i + 1]

        if len(list_slice) >= (i + 1):  # len(lst) < key length = i + 1 (The key length cannot be greater than the list slice)
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
    ciphertext = __read_file(args.encrypted_file[0])
    ciphertext_length = len(ciphertext)

    if args.key is None and args.key_length is None:
        key_length = __get_key_length(ciphertext, ciphertext_length)
        key_shifts = __get_key_shifts(ciphertext, key_length)
        key = __get_key(key_shifts)

    if args.key_length is not None:
        key_length = int(args.key_length[0])
        key_shifts = __get_key_shifts(ciphertext, key_length)
        key = __get_key(key_shifts)

    if args.key is not None:
        key = args.key[0].upper()
        key_length = len(key)
        key_shifts = __get_shifts_from_key(key)

    pt = __decrypt(ciphertext, ciphertext_length, key_shifts, key_length)

    print(f'key: {key}\n')
    print(f'ct: {ciphertext}\n')
    print(f'pt: {pt}\n')
