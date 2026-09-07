class KeyNotFoundError(Exception):
    def __init__(self, key: str) -> None:
        self.message = f"'{key}' does not exist."
        super().__init__(self.message)
