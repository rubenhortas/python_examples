class BasicHashTable:
    def __init__(self, size):
        self._size = size
        self._data: (None | list) = [None] * self._size

    def insert(self, key: str, value: str) -> None:
        index = self._get_index(key)
        self._data[index] = [key, value]

    def get(self, key: str) -> str | None:
        index = self._get_index(key)

        if self._data[index]:
            return self._data[index][1]
        else:
            raise f"'{key}' does not exist."

    def update(self, key: str, value: str) -> None:
        index = self._get_index(key)

        if self._data[index]:
            self._data[index][1] = value
        else:
            raise f"'{key}' does not exist."

    def list(self) -> None:
        index = 0

        for data in self._data:
            if data:
                print(f"[{index}] '{data[0]}': '{data[1]}'")

            index += 1

    def _get_index(self, key: str) -> int:
        result = 0

        for character in key:
            number = ord(character)
            result += number

        index = result % self._size

        return index
