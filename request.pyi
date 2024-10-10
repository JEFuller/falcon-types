from datetime import date
from typing import Iterable

from falcon.stream import BoundedStream


class Request:
    @property
    def bounded_stream(self) -> BoundedStream:
        ...

    @property
    def method(self) -> str:
        ...

    @property
    def path(self) -> str:
        ...

    @property
    def relative_uri(self) -> str:
        ...

    @property
    def params(self) -> dict[str, str]:
        ...

    @property
    def remote_addr(self) -> str:
        ...

    @property
    def content_type(self) -> str | None:
        ...

    def client_prefers(self, media_types: Iterable[str]) -> str:
        ...

    def get_param_as_date(self, name: str, default: date) -> date:
        ...

    @property
    def range(self) -> tuple[int, int]:
        ...
