# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AuthCode(str, enum.Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    DISABLED = "disabled"
    EXPIRED = "expired"
    INVITED = "invited"
    LOCKED = "locked"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        invited: typing.Callable[[], T_Result],
        locked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthCode.SUCCESS:
            return success()
        if self is AuthCode.FAILURE:
            return failure()
        if self is AuthCode.DISABLED:
            return disabled()
        if self is AuthCode.EXPIRED:
            return expired()
        if self is AuthCode.INVITED:
            return invited()
        if self is AuthCode.LOCKED:
            return locked()
