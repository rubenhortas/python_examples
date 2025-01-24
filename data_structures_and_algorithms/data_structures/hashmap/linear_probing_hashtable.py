from data_structures_and_algorithms.data_structures.hashmap.basic_hashtable import BasicHashTable


class LinearProbingHashTable(BasicHashTable):
    def _get_index(self, key: str) -> int:
        index = super()._get_index(key)

        while True:
            if self._data[index] is None or self._data[index][0] == key:
                return index

            index += 1

            if index == self._size:
                index = 0
