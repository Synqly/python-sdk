# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MappingDataType(str, enum.Enum):
    STRING = "string"
    NUMBER = "number"
    DATETIME = "datetime"
    BOOLEAN = "boolean"
    ARRAY = "array"
    ANY = "any"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        array: typing.Callable[[], T_Result],
        any: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MappingDataType.STRING:
            return string()
        if self is MappingDataType.NUMBER:
            return number()
        if self is MappingDataType.DATETIME:
            return datetime()
        if self is MappingDataType.BOOLEAN:
            return boolean()
        if self is MappingDataType.ARRAY:
            return array()
        if self is MappingDataType.ANY:
            return any()
