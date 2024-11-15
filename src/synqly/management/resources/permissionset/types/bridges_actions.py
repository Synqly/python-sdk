# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BridgesActions(str, enum.Enum):
    LIST = "list"
    CREATE = "create"
    GET = "get"
    UPDATE = "update"
    PATCH = "patch"
    DELETE = "delete"
    STATUS = "status"
    ALL = "*"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BridgesActions.LIST:
            return list_()
        if self is BridgesActions.CREATE:
            return create()
        if self is BridgesActions.GET:
            return get()
        if self is BridgesActions.UPDATE:
            return update()
        if self is BridgesActions.PATCH:
            return patch()
        if self is BridgesActions.DELETE:
            return delete()
        if self is BridgesActions.STATUS:
            return status()
        if self is BridgesActions.ALL:
            return all_()
