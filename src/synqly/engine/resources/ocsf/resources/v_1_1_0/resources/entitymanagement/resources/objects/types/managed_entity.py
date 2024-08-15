# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ManagedEntity(pydantic.BaseModel):
    """
    The Managed Entity object describes the type and version of an entity, such as a policy or configuration.
    """

    data: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The managed entity content as a JSON object.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the managed entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The managed entity type. For example: <code>policy</code>, <code>user</code>, <code>organizational unit</code>, <code>device</code>.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the managed entity.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the managed entity. For example: <code>1.2.3</code>.
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