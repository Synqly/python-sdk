# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IntegrationTicketWhen(str, enum.Enum):
    AFTER = "after"
    ASYNC = "async"
    BEFORE = "before"
    DISPLAY = "display"

    def visit(
        self,
        after: typing.Callable[[], T_Result],
        async_: typing.Callable[[], T_Result],
        before: typing.Callable[[], T_Result],
        display: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IntegrationTicketWhen.AFTER:
            return after()
        if self is IntegrationTicketWhen.ASYNC:
            return async_()
        if self is IntegrationTicketWhen.BEFORE:
            return before()
        if self is IntegrationTicketWhen.DISPLAY:
            return display()
