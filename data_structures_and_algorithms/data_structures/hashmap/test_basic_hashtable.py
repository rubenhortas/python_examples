import unittest

from data_structures_and_algorithms.data_structures.hashmap.basic_hashtable import BasicHashTable


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.hashtable = BasicHashTable(15)
        self.hashtable.insert("one", "1")
        self.hashtable.insert("two", "2")
        self.hashtable.insert("three", "3")
        self.hashtable.insert("four", "4")
        self.hashtable.insert("five", "")

    def test_list(self) -> None:
        self.hashtable.list()

    def test_get_value(self) -> None:
        self.assertEqual("1", self.hashtable.get("one"))
        self.assertRaises(BaseException, self.hashtable.get, "six")

    def test_update(self) -> None:
        self.hashtable.update("five", "5")
        self.assertEqual("5", self.hashtable.get("five"))
