# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IntegrationsActions(str, enum.Enum):
    LIST = "list"
    CREATE = "create"
    GET = "get"
    UPDATE = "update"
    PATCH = "patch"
    DELETE = "delete"
    LIST_ACCOUNT = "list_account"
    VERIFY = "verify"
    ALL = "*"

    def visit(
        self,
        list: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        list_account: typing.Callable[[], T_Result],
        verify: typing.Callable[[], T_Result],
        all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IntegrationsActions.LIST:
            return list()
        if self is IntegrationsActions.CREATE:
            return create()
        if self is IntegrationsActions.GET:
            return get()
        if self is IntegrationsActions.UPDATE:
            return update()
        if self is IntegrationsActions.PATCH:
            return patch()
        if self is IntegrationsActions.DELETE:
            return delete()
        if self is IntegrationsActions.LIST_ACCOUNT:
            return list_account()
        if self is IntegrationsActions.VERIFY:
            return verify()
        if self is IntegrationsActions.ALL:
            return all()
