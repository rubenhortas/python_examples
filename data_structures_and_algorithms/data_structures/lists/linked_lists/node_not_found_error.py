class NodeNotFoundError(Exception):
    def __init__(self, data: str) -> None:
        self.message = "Node with data '{data}' not found."
        super().__init__(self.message)
