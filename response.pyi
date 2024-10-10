
from io import BufferedReader
from typing import IO, AnyStr


class Response():

    @property
    def text(self) -> str:
        ...

    @text.setter
    def text(self, value: str) -> None:
        ...

    @property
    def downloadable_as(self) -> None:
        ...

    @downloadable_as.setter
    def downloadable_as(self, value: str) -> None:
        ...

    @property
    def content_type(self) -> str:
        ...

    @content_type.setter
    def content_type(self, value: str) -> None:
        ...

    @property
    def content_length(self) -> int:
        ...

    @content_length.setter
    def content_length(self, value: int) -> None:
        ...

    @property
    def stream(self) -> BufferedReader:
        ...

    @stream.setter
    def stream(self, value: BufferedReader) -> None:
        ...

    def set_stream(self,
                   stream: BufferedReader | IO[AnyStr],
                   content_length: int) -> None:
        ...

    @property
    def data(self) -> bytes:
        ...

    @data.setter
    def data(self, value: bytes) -> None:
        ...

    @property
    def accept_ranges(self) -> str:
        ...

    @accept_ranges.setter
    def accept_ranges(self, value: str) -> None:
        ...

    @property
    def status(self) -> str:
        ...

    @status.setter
    def status(self, value: str) -> None:
        ...

    def append_header(self, name: str, value: str) -> None:
        ...
