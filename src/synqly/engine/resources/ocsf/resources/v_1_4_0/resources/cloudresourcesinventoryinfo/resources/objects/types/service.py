# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .key_value_object import KeyValueObject

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Service(pydantic.BaseModel):
    """
    The Service object describes characteristics of a service, <code> e.g. AWS EC2. </code>
    """

    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of labels associated with the service.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the service.
    """

    tags: typing.Optional[typing.List[KeyValueObject]] = pydantic.Field(default=None)
    """
    The list of tags; <code>{key:value}</code> pairs associated to the service.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the service.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the service.
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
