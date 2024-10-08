# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BridgeType(str, enum.Enum):
    BRIDGE_AWS = "bridge_aws"
    BRIDGE_AWS_ID = "bridge_aws_id"
    BRIDGE_TOKEN = "bridge_token"
    BRIDGE_TOKEN_ID = "bridge_token_id"
    BRIDGE_BASIC = "bridge_basic"
    BRIDGE_BASIC_ID = "bridge_basic_id"
    BRIDGE_SECRET = "bridge_secret"
    BRIDGE_SECRET_ID = "bridge_secret_id"
    BRIDGE_O_AUTH_CLIENT = "bridge_o_auth_client"
    BRIDGE_O_AUTH_CLIENT_ID = "bridge_o_auth_client_id"

    def visit(
        self,
        bridge_aws: typing.Callable[[], T_Result],
        bridge_aws_id: typing.Callable[[], T_Result],
        bridge_token: typing.Callable[[], T_Result],
        bridge_token_id: typing.Callable[[], T_Result],
        bridge_basic: typing.Callable[[], T_Result],
        bridge_basic_id: typing.Callable[[], T_Result],
        bridge_secret: typing.Callable[[], T_Result],
        bridge_secret_id: typing.Callable[[], T_Result],
        bridge_o_auth_client: typing.Callable[[], T_Result],
        bridge_o_auth_client_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BridgeType.BRIDGE_AWS:
            return bridge_aws()
        if self is BridgeType.BRIDGE_AWS_ID:
            return bridge_aws_id()
        if self is BridgeType.BRIDGE_TOKEN:
            return bridge_token()
        if self is BridgeType.BRIDGE_TOKEN_ID:
            return bridge_token_id()
        if self is BridgeType.BRIDGE_BASIC:
            return bridge_basic()
        if self is BridgeType.BRIDGE_BASIC_ID:
            return bridge_basic_id()
        if self is BridgeType.BRIDGE_SECRET:
            return bridge_secret()
        if self is BridgeType.BRIDGE_SECRET_ID:
            return bridge_secret_id()
        if self is BridgeType.BRIDGE_O_AUTH_CLIENT:
            return bridge_o_auth_client()
        if self is BridgeType.BRIDGE_O_AUTH_CLIENT_ID:
            return bridge_o_auth_client_id()
