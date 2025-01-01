from data_structures_and_algorithms.data_structures.hashmap.basic_hashtable import BasicHashTable


class LinearProbingHashTable(BasicHashTable):
    def _get_index(self, key: str) -> int:
        def get_index():
            result = 0

            for character in key:
                number = ord(character)
                result += number

            index = result % self._size

            return index

        index = get_index()

        while True:
            if self._data[index] is None or self._data[index][0] == key:
                return index

            index += 1

            if index == self._size:
                index = 0
