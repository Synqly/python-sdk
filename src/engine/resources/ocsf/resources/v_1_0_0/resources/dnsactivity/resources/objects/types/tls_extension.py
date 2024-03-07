# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .tls_extension_type_id import TlsExtensionTypeId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TlsExtension(pydantic.BaseModel):
    """
    The TLS Extension object describes additional attributes that extend the base Transport Layer Security (TLS) object.
    """

    data: typing.Optional[typing.Any] = pydantic.Field(
        description="The data contains information specific to the particular extension type."
    )
    type: typing.Optional[str] = pydantic.Field(
        description="The TLS extension type. For example: <code>Server Name</code>."
    )
    type_id: TlsExtensionTypeId = pydantic.Field(
        description="The TLS extension type identifier. See <a target='_blank' href='https://datatracker.ietf.org/doc/html/rfc8446#page-35'>The Transport Layer Security (TLS) extension page</a>."
    )

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
