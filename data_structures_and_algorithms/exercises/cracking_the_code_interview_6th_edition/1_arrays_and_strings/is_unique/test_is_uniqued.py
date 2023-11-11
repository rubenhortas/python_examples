#!/usr/bin/env python3

import unittest

from is_unique import is_unique, is_unique_without_structures, is_unique_set, is_unique_counter, is_unique_count


class TestIsUnique(unittest.TestCase):
    def setUp(self):
        self.unique = 'abcdefghij'
        self.not_unique = "abcdefabcd"

    def test_is_unique(self):
        self.assertTrue(is_unique(self.unique))
        self.assertFalse(is_unique(self.not_unique))

    def test_is_unique_without_structures(self):
        self.assertTrue(is_unique_without_structures(self.unique))
        self.assertFalse(is_unique_without_structures(self.not_unique))

    def test_is_unique_set(self):
        self.assertTrue(is_unique_set(self.unique))
        self.assertFalse(is_unique_set(self.not_unique))

    def test_is_unique_counter(self):
        self.assertTrue(is_unique_counter(self.unique))
        self.assertFalse(is_unique_counter(self.not_unique))

    def test_is_unique_count(self):
        self.assertTrue(is_unique_count(self.unique))
        self.assertFalse(is_unique_count(self.not_unique))
