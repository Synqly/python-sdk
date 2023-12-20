# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class San(pydantic.BaseModel):
    """
    The Subject Alternative name (SAN) object describes a SAN secured by a digital certificate
    """

    name: str = pydantic.Field(description="Name of SAN (e.g. The actual IP Address or domain.)")
    type: str = pydantic.Field(description="Type descriptor of SAN (e.g. IP Address/domain/etc.)")

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
