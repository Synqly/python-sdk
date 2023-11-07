# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime


class Metric(pydantic.BaseModel):
    """
    The Metric object defines a simple name/value pair entity for a metric.
    """

    name: str = pydantic.Field(description="The name of the metric.")
    value: str = pydantic.Field(description="The value of the metric.")

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
