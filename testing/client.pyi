from typing import Any, NotRequired, TypedDict, Unpack


class Result:

    @property
    def status_code(self) -> int:
        ...

    @property
    def content(self) -> bytes:
        ...

    @property
    def json(self) -> dict[Any, Any]:
        ...

    @property
    def text(self) -> str:
        ...

    @property
    def headers(self) -> dict[str, str]:
        ...


class GetParams(TypedDict):
    headers: NotRequired[dict[str, str]]


class PostParams(TypedDict):
    body: NotRequired[str]
    params: NotRequired[dict[str, Any]]


class TestClient:
    def simulate_get(self, path: str, **kwargs: Unpack[GetParams]) -> Result:
        ...

    def simulate_post(self, path: str, **kwargs: Unpack[PostParams]) -> Result:
        ...
