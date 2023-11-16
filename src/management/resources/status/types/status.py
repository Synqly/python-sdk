# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...accounts.types.account_id import AccountId
from ...integrations.types.integration_id import IntegrationId


class Status(pydantic.BaseModel):
    """
    Status object
    """

    created_at: dt.datetime = pydantic.Field(description="Time object was originally created")
    updated_at: dt.datetime = pydantic.Field(description="Last time object was updated")
    account_id: AccountId = pydantic.Field(description="Account owner")
    integration_id: IntegrationId = pydantic.Field(description="Integration object")
    status: str = pydantic.Field(description="The current status of the notification.")
    requests: int = pydantic.Field(description="Request count")
    failed: int = pydantic.Field(description="Failed count")
    cpu_time: int = pydantic.Field(description="Cpu time in microseconds")
    db_ops: int = pydantic.Field(description="Database operations count")
    api_ops: int = pydantic.Field(description="API operations count")
    in_bytes: int = pydantic.Field(description="API input byte count")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
