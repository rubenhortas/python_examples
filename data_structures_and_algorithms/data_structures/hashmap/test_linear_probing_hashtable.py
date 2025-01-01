import unittest

from data_structures_and_algorithms.data_structures.hashmap.linear_probing_hashtable import LinearProbingHashTable


class Test(unittest.TestCase):
    def setUp(self):
        self.hashtable = LinearProbingHashTable(15)
        self.hashtable.insert('listen', 'l')
        self.hashtable.insert('silent', 's')
        self.hashtable.insert('music', 'm')

    def test_list(self):
        self.hashtable.list()

    def test_get_value(self):
        self.assertEqual('l', self.hashtable.get('listen'))
        self.assertRaises(BaseException, self.hashtable.get, 'play')

    def test_update(self):
        self.hashtable.update('music', 'M')
        self.assertEqual('M', self.hashtable.get('music'))
