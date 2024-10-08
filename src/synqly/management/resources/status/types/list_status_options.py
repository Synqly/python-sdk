# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListStatusOptions(str, enum.Enum):
    ACCOUNT = "account"
    ACCOUNTS = "accounts"
    INTEGRATION = "integration"
    INTEGRATIONS = "integrations"
    ALL = "all"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        accounts: typing.Callable[[], T_Result],
        integration: typing.Callable[[], T_Result],
        integrations: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListStatusOptions.ACCOUNT:
            return account()
        if self is ListStatusOptions.ACCOUNTS:
            return accounts()
        if self is ListStatusOptions.INTEGRATION:
            return integration()
        if self is ListStatusOptions.INTEGRATIONS:
            return integrations()
        if self is ListStatusOptions.ALL:
            return all_()
