# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...base.types.url_string import UrlString
from .reputation import Reputation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Enrichment(pydantic.BaseModel):
    """
    The Enrichment object provides inline enrichment data for specific attributes of interest within an event. It serves as a mechanism to enhance or supplement the information associated with the event by adding additional relevant details or context.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the enrichment data was generated.
    """

    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the enrichment data was generated.
    """

    data: typing.Any = pydantic.Field()
    """
    The enrichment data associated with the attribute and value. The meaning of this data depends on the type the enrichment record.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    A long description of the enrichment data.
    """

    name: str = pydantic.Field()
    """
    The name of the attribute to which the enriched data pertains.
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    The enrichment data provider name.
    """

    reputation: typing.Optional[Reputation] = pydantic.Field(default=None)
    """
    The reputation of the enrichment data.
    """

    short_desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of the enrichment data.
    """

    src_url: typing.Optional[UrlString] = pydantic.Field(default=None)
    """
    The URL of the source of the enrichment data.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The enrichment type. For example: <code>location</code>.
    """

    value: str = pydantic.Field()
    """
    The value of the attribute to which the enriched data pertains.
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