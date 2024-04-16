# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectionState(str, enum.Enum):
    CONNECT = "Connect"
    DISCONNECT = "Disconnect"

    def visit(self, connect: typing.Callable[[], T_Result], disconnect: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionState.CONNECT:
            return connect()
        if self is ConnectionState.DISCONNECT:
            return disconnect()
