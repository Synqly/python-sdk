# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CredentialsActions(str, enum.Enum):
    LIST = "list"
    CREATE = "create"
    GET = "get"
    UPDATE = "update"
    PATCH = "patch"
    DELETE = "delete"
    ALL = "*"

    def visit(
        self,
        list: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CredentialsActions.LIST:
            return list()
        if self is CredentialsActions.CREATE:
            return create()
        if self is CredentialsActions.GET:
            return get()
        if self is CredentialsActions.UPDATE:
            return update()
        if self is CredentialsActions.PATCH:
            return patch()
        if self is CredentialsActions.DELETE:
            return delete()
        if self is CredentialsActions.ALL:
            return all()
