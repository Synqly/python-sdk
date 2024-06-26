# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WebhooksActions(str, enum.Enum):
    LIST = "list"
    CREATE = "create"
    GET = "get"
    UPDATE = "update"
    PATCH = "patch"
    DELETE = "delete"
    ALL = "*"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhooksActions.LIST:
            return list_()
        if self is WebhooksActions.CREATE:
            return create()
        if self is WebhooksActions.GET:
            return get()
        if self is WebhooksActions.UPDATE:
            return update()
        if self is WebhooksActions.PATCH:
            return patch()
        if self is WebhooksActions.DELETE:
            return delete()
        if self is WebhooksActions.ALL:
            return all_()
