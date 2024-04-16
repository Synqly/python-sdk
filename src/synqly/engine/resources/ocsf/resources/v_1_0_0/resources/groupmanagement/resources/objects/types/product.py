# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.url_string import UrlString
from .feature import Feature

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Product(pydantic.BaseModel):
    """
    The Product object describes characteristics of a software product.
    """

    feature: typing.Optional[Feature] = pydantic.Field(default=None)
    """
    The feature that reported the event.
    """

    lang: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two letter lower case language codes, as defined by <a target='_blank' href='https://en.wikipedia.org/wiki/ISO_639-1'>ISO 639-1</a>. For example: <code>en</code> (English), <code>de</code> (German), or <code>fr</code> (French).
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the product.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The installation path of the product.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the product.
    """

    url_string: typing.Optional[UrlString] = pydantic.Field(default=None)
    """
    The URL pointing towards the product.
    """

    vendor_name: str = pydantic.Field()
    """
    The name of the vendor of the product.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the product, as defined by the event source. For example: <code>2013.1.3-beta</code>.
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
