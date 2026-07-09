class EmptyListError(Exception):
    def __init__(self) -> None:
        self.message = "Empty list."
        super().__init__(self.message)
