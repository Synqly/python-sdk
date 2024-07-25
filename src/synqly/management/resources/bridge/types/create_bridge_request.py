# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateBridgeRequest(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique short name for this Bridge (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to BridgeGroupId if both name and fullname are not specified.
    """

    fullname: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human friendly display name for this Bridge, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the resources included in the bridge and permissions granted on those resources. Includes details of when to use this bridge along with the intended personas.
    """

    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Bridge selection labels
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
