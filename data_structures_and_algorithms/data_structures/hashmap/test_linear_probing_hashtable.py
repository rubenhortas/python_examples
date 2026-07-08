import unittest

from data_structures_and_algorithms.data_structures.hashmap.key_not_found_error import KeyNotFoundError
from data_structures_and_algorithms.data_structures.hashmap.linear_probing_hashtable import LinearProbingHashTable


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.hashtable = LinearProbingHashTable(15)
        self.hashtable.insert("listen", "l")
        self.hashtable.insert("silent", "s")
        self.hashtable.insert("music", "m")

    def test_list(self) -> None:
        self.hashtable.list()

    def test_get_value(self) -> None:
        self.assertEqual("l", self.hashtable.get("listen"))
        self.assertRaises(KeyNotFoundError, self.hashtable.get, "play")

    def test_update(self) -> None:
        self.hashtable.update("music", "M")
        self.assertEqual("M", self.hashtable.get("music"))
