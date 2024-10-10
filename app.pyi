from typing import Any, Callable, TypeVar

from falcon.request import Request
from falcon.response import Response
from falcon.routing.converters import BaseConverter


class RouterOptions:
    converters: dict[str, type[BaseConverter]]


T = TypeVar('T', bound=Request)
ErrorSerializer = Callable[[T, Response, Any], None]


class App:
    router_options: RouterOptions

    def __init__(self, middleware: Any, request_type: Any = None) -> None: ...

    def add_route(self, path: str, resource: Any, suffix: str | None = None) -> None:
        ...

    def set_error_serializer(
        self, serialize_error: ErrorSerializer[T]) -> None: ...
