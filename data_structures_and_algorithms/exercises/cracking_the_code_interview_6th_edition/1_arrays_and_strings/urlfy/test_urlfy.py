#!/usr/bin/env python3

import unittest

from urlfy import get_url, get_url_pythonic


class TestUrlfy(unittest.TestCase):
    def setUp(self):
        self.string = "Mr John Smith    "  # length = 17, "true" length = 13
        self.true_length = 13
        self.url = "Mr%20John%20Smith"

    def test_get_url(self):
        # We will use a list because, in python, strings are immutable
        result = get_url(list(self.string), self.true_length)

        self.assertEqual(result, list(self.url))
        self.assertEqual(len(result), len(self.string))

    def test_get_url_pythonic(self):
        # We will use a list because, in python, strings are immutable
        result = get_url_pythonic(list(self.string), self.true_length)

        self.assertEqual(result, list(self.url))
        self.assertEqual(len(result), len(self.string))
