# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class HttpMethod(str, enum.Enum):
    GET = "GET"
    PATCH = "PATCH"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HttpMethod.GET:
            return get()
        if self is HttpMethod.PATCH:
            return patch()
        if self is HttpMethod.POST:
            return post()
        if self is HttpMethod.PUT:
            return put()
        if self is HttpMethod.DELETE:
            return delete()
