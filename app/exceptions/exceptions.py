class NotFoundError(Exception):
    def __init__(self, message: str = "Resource not found"):
        self.message = message
        super().__init__(self.message)


class BadRequestError(Exception):
    def __init__(self, message: str = "Bad request"):
        self.message = message
        super().__init__(self.message)