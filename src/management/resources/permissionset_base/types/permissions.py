# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Permissions(str, enum.Enum):
    ADMINISTRATOR = "administrator"
    VIEWER = "viewer"
    MEMBER = "member"
    ACCOUNT_MANAGER = "account-manager"

    def visit(
        self,
        administrator: typing.Callable[[], T_Result],
        viewer: typing.Callable[[], T_Result],
        member: typing.Callable[[], T_Result],
        account_manager: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Permissions.ADMINISTRATOR:
            return administrator()
        if self is Permissions.VIEWER:
            return viewer()
        if self is Permissions.MEMBER:
            return member()
        if self is Permissions.ACCOUNT_MANAGER:
            return account_manager()