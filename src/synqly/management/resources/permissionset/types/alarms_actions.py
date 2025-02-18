# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AlarmsActions(str, enum.Enum):
    LIST = "list"
    GET = "get"
    MODE = "mode"
    PRIORITY = "priority"
    CLEAR = "clear"
    ALL = "*"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        mode: typing.Callable[[], T_Result],
        priority: typing.Callable[[], T_Result],
        clear: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlarmsActions.LIST:
            return list_()
        if self is AlarmsActions.GET:
            return get()
        if self is AlarmsActions.MODE:
            return mode()
        if self is AlarmsActions.PRIORITY:
            return priority()
        if self is AlarmsActions.CLEAR:
            return clear()
        if self is AlarmsActions.ALL:
            return all_()
