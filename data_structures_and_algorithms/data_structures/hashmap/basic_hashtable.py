from data_structures_and_algorithms.data_structures.hashmap.hashtable import HashTable


class BasicHashTable(HashTable):
    def _get_index(self, key: str) -> int:
        result = 0

        for character in key:
            number = ord(character)
            result += number

        index = result % self._size

        return index
