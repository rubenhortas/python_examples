from data_structures_and_algorithms.data_structures.hashmap.key_not_found_error import KeyNotFoundError


class HashTable:
    def __init__(self, size: int) -> None:
        self._size = size
        self._data: list[None | list[str]] = [None] * self._size

    def insert(self, key: str, value: str) -> None:
        index = self._get_index(key)
        self._data[index] = [key, value]

    def get(self, key: str) -> str | None:
        index = self._get_index(key)

        if self._data[index]:
            return self._data[index][1]
        else:
            raise KeyNotFoundError(key)

    def update(self, key: str, value: str) -> None:
        index = self._get_index(key)

        if self._data[index]:
            self._data[index][1] = value
        else:
            raise KeyNotFoundError(key)

    def list(self) -> None:
        for index, data in enumerate(self._data):
            if data:
                print(f"[{index}] '{data[0]}': '{data[1]}'")

    def _get_index(self, key: str) -> int:  # noqa: ARG002
        raise KeyNotFoundError("")
