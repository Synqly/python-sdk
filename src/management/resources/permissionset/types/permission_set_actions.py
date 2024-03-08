# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PermissionSetActions(str, enum.Enum):
    LIST = "list"
    GET = "get"
    ALL = "*"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PermissionSetActions.LIST:
            return list_()
        if self is PermissionSetActions.GET:
            return get()
        if self is PermissionSetActions.ALL:
            return all_()
