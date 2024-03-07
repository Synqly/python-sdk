# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...base.types.url_string import UrlString
from .related_event import RelatedEvent
from .remediation import Remediation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Finding(pydantic.BaseModel):
    """
    The Finding object describes metadata related to a security finding generated by a security tool or system.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(description="The time when the finding was created.")
    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(description="The time when the finding was created.")
    desc: typing.Optional[str] = pydantic.Field(description="The description of the reported finding.")
    first_seen_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The time when the finding was first observed."
    )
    first_seen_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The time when the finding was first observed."
    )
    last_seen_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The time when the finding was most recently observed."
    )
    last_seen_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The time when the finding was most recently observed."
    )
    modified_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The time when the finding was last modified."
    )
    modified_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The time when the finding was last modified."
    )
    product_uid: typing.Optional[str] = pydantic.Field(
        description="The unique identifier of the product that reported the finding."
    )
    related_events: typing.Optional[typing.List[RelatedEvent]] = pydantic.Field(
        description="Describes events and/or other findings related to the finding as identified by the security product."
    )
    remediation: typing.Optional[Remediation] = pydantic.Field(
        description="Describes the recommended remediation steps to address identified issue(s)."
    )
    src_url: typing.Optional[UrlString] = pydantic.Field(description="The URL pointing to the source of the finding.")
    supporting_data: typing.Optional[typing.Any] = pydantic.Field(
        description="Additional data supporting a finding as provided by security tool"
    )
    title: str = pydantic.Field(description="A title or a brief phrase summarizing the reported finding.")
    types: typing.Optional[typing.List[str]] = pydantic.Field(description="One or more types of the reported finding.")
    uid: str = pydantic.Field(description="The unique identifier of the reported finding.")

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
