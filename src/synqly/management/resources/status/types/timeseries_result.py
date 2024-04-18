# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TimeseriesResult(pydantic.BaseModel):
    """
    Status timeseries object
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Interval time
    """

    succeeded: int = pydantic.Field()
    """
    Succeeded count
    """

    failed: int = pydantic.Field()
    """
    Failed count
    """

    cpu_time: int = pydantic.Field()
    """
    Cpu time in microseconds
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