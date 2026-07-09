class MethodNotImplementedError(Exception):
    def __init__(self) -> None:
        self.message = "Method not implemented."
        super().__init__(self.message)
