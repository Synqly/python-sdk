# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OwnerType(str, enum.Enum):
    ACCOUNT = "account"
    INTEGRATION_POINT = "integration_point"

    def visit(
        self, account: typing.Callable[[], T_Result], integration_point: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is OwnerType.ACCOUNT:
            return account()
        if self is OwnerType.INTEGRATION_POINT:
            return integration_point()