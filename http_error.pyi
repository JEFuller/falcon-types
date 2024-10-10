class HTTPError(Exception):
    status: str
    title: str

    def __init__(self, status: str, title: str) -> None:
        ...
