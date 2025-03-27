# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Priority(str, enum.Enum):
    URGENT = "URGENT"
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    MODERATE = "MODERATE"
    LOW = "LOW"
    PLANNING = "PLANNING"

    def visit(
        self,
        urgent: typing.Callable[[], T_Result],
        critical: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        moderate: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        planning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Priority.URGENT:
            return urgent()
        if self is Priority.CRITICAL:
            return critical()
        if self is Priority.HIGH:
            return high()
        if self is Priority.MEDIUM:
            return medium()
        if self is Priority.MODERATE:
            return moderate()
        if self is Priority.LOW:
            return low()
        if self is Priority.PLANNING:
            return planning()
