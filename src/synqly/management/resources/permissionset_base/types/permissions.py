# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Permissions(str, enum.Enum):
    ADMINISTRATOR = "administrator"
    VIEWER = "viewer"
    MEMBER = "member"
    ACCOUNT_MANAGER = "account-manager"
    CONNECT_UI = "connect-ui"
    TOKEN_ISSUER = "token-issuer"
    MCP_INTEGRATIONS_USE_ONLY = "mcp-integrations-use-only"
    """
    Permission set that provides the minimum level of access necessary for MCP use. Gives read access to accounts and integrations and the ability to use any Connector API.
    """

    def visit(
        self,
        administrator: typing.Callable[[], T_Result],
        viewer: typing.Callable[[], T_Result],
        member: typing.Callable[[], T_Result],
        account_manager: typing.Callable[[], T_Result],
        connect_ui: typing.Callable[[], T_Result],
        token_issuer: typing.Callable[[], T_Result],
        mcp_integrations_use_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Permissions.ADMINISTRATOR:
            return administrator()
        if self is Permissions.VIEWER:
            return viewer()
        if self is Permissions.MEMBER:
            return member()
        if self is Permissions.ACCOUNT_MANAGER:
            return account_manager()
        if self is Permissions.CONNECT_UI:
            return connect_ui()
        if self is Permissions.TOKEN_ISSUER:
            return token_issuer()
        if self is Permissions.MCP_INTEGRATIONS_USE_ONLY:
            return mcp_integrations_use_only()
