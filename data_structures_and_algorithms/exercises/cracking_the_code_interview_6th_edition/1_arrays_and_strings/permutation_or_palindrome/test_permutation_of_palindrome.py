#!/usr/bin/env python3

import unittest

from permutation_of_palindrome import is_permutation_of_palindrome, is_permutation_of_palindrome_pythonic


class TestPermutationOfPalindrome(unittest.TestCase):
    def setUp(self):
        self.data = [
            ('Tact Coa', True),
            ('t a c t coapapa', True),
            ('Tact Coax', False),
            ('asdfadfadf', False)
        ]

    def test_is_permutation_of_palindrome(self):
        for string, result in self.data:
            self.assertEqual(is_permutation_of_palindrome(string), result)

    def test_is_permutation_of_palindrome_pythonic(self):
        for string, result in self.data:
            self.assertEqual(is_permutation_of_palindrome_pythonic(string), result)
