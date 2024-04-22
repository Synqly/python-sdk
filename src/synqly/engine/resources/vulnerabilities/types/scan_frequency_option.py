# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ScanFrequencyOption(str, enum.Enum):
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    UNKNOWN = "unknown"

    def visit(
        self,
        once: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        yearly: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScanFrequencyOption.ONCE:
            return once()
        if self is ScanFrequencyOption.DAILY:
            return daily()
        if self is ScanFrequencyOption.WEEKLY:
            return weekly()
        if self is ScanFrequencyOption.MONTHLY:
            return monthly()
        if self is ScanFrequencyOption.YEARLY:
            return yearly()
        if self is ScanFrequencyOption.UNKNOWN:
            return unknown()
