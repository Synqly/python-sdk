# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class QueryEventStatus(str, enum.Enum):
    PENDING = "PENDING"
    COMPLETE = "COMPLETE"

    def visit(self, pending: typing.Callable[[], T_Result], complete: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryEventStatus.PENDING:
            return pending()
        if self is QueryEventStatus.COMPLETE:
            return complete()
