class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def insert(self, key: str, value: str) -> None:
        index = self._get_index(key)
        self.data[index] = [key, value]

    def get(self, key: str) -> str | None:
        index = self._get_index(key)

        if self.data[index]:
            return self.data[index][1]
        else:
            raise f"'{key}' does not exists."

    def update(self, key: str, value: str) -> None:
        index = self._get_index(key)

        if self.data[index]:
            self.data[index][1] = value
        else:
            raise f"'{key}' does not exists."

    def list(self) -> None:
        for data in self.data:
            if data:
                print(f"'{data[0]}': '{data[1]}'")

    def _get_index(self, string: str) -> int:
        result = 0

        for character in string:
            number = ord(character)
            result += number

        index = result % self.size

        return index
