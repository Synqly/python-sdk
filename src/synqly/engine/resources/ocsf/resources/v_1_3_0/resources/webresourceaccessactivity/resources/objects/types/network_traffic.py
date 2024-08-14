# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NetworkTraffic(pydantic.BaseModel):
    """
    The Network Traffic object describes characteristics of network traffic. Network traffic refers to data moving across a network at a given point of time. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:NetworkTraffic/'>d3f:NetworkTraffic</a>.
    """

    bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of bytes (in and out).
    """

    bytes_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of bytes sent from the destination to the source.
    """

    bytes_out: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of bytes sent from the source to the destination.
    """

    chunks: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of chunks (in and out).
    """

    chunks_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of chunks sent from the destination to the source.
    """

    chunks_out: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of chunks sent from the source to the destination.
    """

    packets: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of packets (in and out).
    """

    packets_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of packets sent from the destination to the source.
    """

    packets_out: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of packets sent from the source to the destination.
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
