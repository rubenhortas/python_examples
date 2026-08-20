class NodeNotFoundError(Exception):
    def __init__(self, _data: str) -> None:
        self.message = "Node with value '{_data}' not found."
        super().__init__(self.message)
