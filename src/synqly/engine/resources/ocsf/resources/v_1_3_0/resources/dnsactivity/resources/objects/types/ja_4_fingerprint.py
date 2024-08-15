# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .ja_4_fingerprint_type_id import Ja4FingerprintTypeId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Ja4Fingerprint(pydantic.BaseModel):
    """
    The JA4+ fingerprint object provides detailed fingerprint information about various aspects of network traffic which is both machine and human readable.
    """

    section_a: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 'a' section of the JA4 fingerprint.
    """

    section_b: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 'b' section of the JA4 fingerprint.
    """

    section_c: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 'c' section of the JA4 fingerprint.
    """

    section_d: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 'd' section of the JA4 fingerprint.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The JA4+ fingerprint type as defined by <a href='https://blog.foxio.io/ja4+-network-fingerprinting target='\_blank'>FoxIO</a>, normalized to the caption of 'type_id'. In the case of 'Other', it is defined by the event source.
    """

    type_id: Ja4FingerprintTypeId = pydantic.Field()
    """
    The identifier of the JA4+ fingerprint type.
    """

    value: str = pydantic.Field()
    """
    The JA4+ fingerprint value.
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