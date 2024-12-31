import unittest

from data_structures_and_algorithms.data_structures.hashmap.hashtable import HashTable


class Test(unittest.TestCase):
    def setUp(self):
        self.hashtable = HashTable(444)
        self.hashtable.insert('one', '1')
        self.hashtable.insert('two', '2')
        self.hashtable.insert('three', '3')
        self.hashtable.insert('four', '4')
        self.hashtable.insert('five', '')

    def test_list(self):
        self.hashtable.list()
        return True

    def test_get_value(self):
        self.assertEqual('1', self.hashtable.get('one'))
        self.assertRaises(BaseException, self.hashtable.get, 'six')

    def test_update(self):
        self.hashtable.update('five', '5')
        self.assertEqual('5', self.hashtable.get('five'))
