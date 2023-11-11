#!/usr/bin/env python3

import unittest

from check_permutation import is_permutation_sorting, is_permutation, is_permutation_count


class CheckPermutationTest(unittest.TestCase):
    def setUp(self):
        self.string1 = 'check permutations'
        self.string2 = 'permutations check'
        self.string3 = 'p3rmut4t10n5 ch3ck'
        self.string4 = 'permutations check '

    def test_is_permutation_sorting(self):
        result = is_permutation_sorting(self.string1, self.string2)
        self.assertTrue(result)

        result = is_permutation_sorting(self.string1, self.string3)
        self.assertFalse(result)

        result = is_permutation_sorting(self.string1, self.string4)
        self.assertFalse(result)

        result = is_permutation_sorting("", "")
        self.assertTrue(result)

    def test_check_is_permutation(self):
        result = is_permutation(self.string1, self.string2)
        self.assertTrue(result)

        result = is_permutation(self.string1, self.string3)
        self.assertFalse(result)

        result = is_permutation_sorting(self.string1, self.string4)
        self.assertFalse(result)

        result = is_permutation_sorting("", "")
        self.assertTrue(result)

    def test_is_permutation_count(self):
        result = is_permutation_count(self.string1, self.string2)
        self.assertTrue(result)

        result = is_permutation_count(self.string1, self.string3)
        self.assertFalse(result)

        result = is_permutation_sorting(self.string1, self.string4)
        self.assertFalse(result)

        result = is_permutation_sorting("", "")
        self.assertTrue(result)
