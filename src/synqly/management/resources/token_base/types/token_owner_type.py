# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TokenOwnerType(str, enum.Enum):
    ORGANIZATION = "organization"
    INTEGRATION = "integration"

    def visit(
        self, organization: typing.Callable[[], T_Result], integration: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TokenOwnerType.ORGANIZATION:
            return organization()
        if self is TokenOwnerType.INTEGRATION:
            return integration()