# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StatusActions(str, enum.Enum):
    LIST = "list"
    GET = "get"
    RESET = "reset"
    LIST_EVENTS = "list_events"
    TIMESERIES = "timeseries"
    INTEGRATION_TIMESERIES = "integration_timeseries"
    ALL = "*"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        reset: typing.Callable[[], T_Result],
        list_events: typing.Callable[[], T_Result],
        timeseries: typing.Callable[[], T_Result],
        integration_timeseries: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusActions.LIST:
            return list_()
        if self is StatusActions.GET:
            return get()
        if self is StatusActions.RESET:
            return reset()
        if self is StatusActions.LIST_EVENTS:
            return list_events()
        if self is StatusActions.TIMESERIES:
            return timeseries()
        if self is StatusActions.INTEGRATION_TIMESERIES:
            return integration_timeseries()
        if self is StatusActions.ALL:
            return all_()
