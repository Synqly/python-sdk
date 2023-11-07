# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...common.types.id import Id
from .http_method import HttpMethod


class Audit(pydantic.BaseModel):
    environment: str
    created_at: dt.datetime = pydantic.Field(description="Time when the API request occurred.")
    method: HttpMethod
    path: str
    code: str
    status: str
    body: typing.Optional[typing.Any]
    integration_id: typing.Optional[Id]

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
