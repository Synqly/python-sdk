# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...accounts.types.account_id import AccountId
from ...integration_base.types.integration_id import IntegrationId
from ...member_base.types.member_id import MemberId
from .http_method import HttpMethod

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Audit(pydantic.BaseModel):
    environment: str
    created_at: dt.datetime = pydantic.Field(description="Time when the API request occurred.")
    remote_addr: str
    user_agent: str
    method: HttpMethod
    path: str
    code: str
    body: typing.Optional[typing.Any]
    response: typing.Optional[str]
    status: typing.Optional[str]
    member_id: typing.Optional[MemberId]
    account_id: typing.Optional[AccountId]
    integration_id: typing.Optional[IntegrationId]

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
