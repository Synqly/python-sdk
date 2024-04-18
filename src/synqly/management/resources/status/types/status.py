# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...accounts.types.account import Account
from ...accounts.types.account_id import AccountId
from ...integration_base.types.integration_id import IntegrationId
from ...integrations.types.integration import Integration

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Status(pydantic.BaseModel):
    """
    Status object
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Time object was originally created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Last time object was updated
    """

    account_id: AccountId = pydantic.Field()
    """
    Account owner
    """

    account: typing.Optional[Account] = pydantic.Field(default=None)
    """
    Optional `ListStatusResponse` only; expand Account object
    """

    integration_id: IntegrationId = pydantic.Field()
    """
    Integration object
    """

    integration: typing.Optional[Integration] = pydantic.Field(default=None)
    """
    Optional `ListStatusResponse` only; expand Integration object
    """

    status: str = pydantic.Field()
    """
    The current status of the notification.
    """

    requests: int = pydantic.Field()
    """
    Request count
    """

    failed: int = pydantic.Field()
    """
    Failed count
    """

    cpu_time: int = pydantic.Field()
    """
    Cpu time in microseconds
    """

    db_ops: int = pydantic.Field()
    """
    Database operations count
    """

    api_ops: int = pydantic.Field()
    """
    API operations count
    """

    in_bytes: int = pydantic.Field()
    """
    API input byte count
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}