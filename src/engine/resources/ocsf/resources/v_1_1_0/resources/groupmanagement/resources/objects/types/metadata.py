# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from .extension import Extension
from .logger import Logger
from .product import Product

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Metadata(pydantic.BaseModel):
    """
    The Metadata object describes the metadata associated with the event. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:Metadata/'>d3f:Metadata</a>.
    """

    correlation_uid: typing.Optional[str] = pydantic.Field(
        description="The unique identifier used to correlate events."
    )
    event_code: typing.Optional[str] = pydantic.Field(
        description="The Event ID or Code that the product uses to describe the event."
    )
    extension: typing.Optional[Extension] = pydantic.Field(description="The schema extension used to create the event.")
    extensions: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="The schema extensions used to create the event."
    )
    labels: typing.Optional[typing.List[str]] = pydantic.Field(
        description='<p>The list of category labels attached to the event or specific attributes. Labels are user defined tags or aliases added at normalization time.</p>For example: <code>["network", "connection.ip:destination", "device.ip:source"]</code>'
    )
    log_level: typing.Optional[str] = pydantic.Field(description="The audit level at which an event was generated.")
    log_name: typing.Optional[str] = pydantic.Field(
        description="The event log name. For example, syslog file name or Windows logging subsystem: Security."
    )
    log_provider: typing.Optional[str] = pydantic.Field(
        description="The logging provider or logging service that logged the event. For example, Microsoft-Windows-Security-Auditing."
    )
    log_version: typing.Optional[str] = pydantic.Field(
        description="The event log schema version that specifies the format of the original event. For example syslog version or Cisco Log Schema Version."
    )
    logged_time: typing.Optional[Timestamp] = pydantic.Field(
        description="<p>The time when the logging system collected and logged the event.</p>This attribute is distinct from the event time in that event time typically contain the time extracted from the original event. Most of the time, these two times will be different."
    )
    logged_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="<p>The time when the logging system collected and logged the event.</p>This attribute is distinct from the event time in that event time typically contain the time extracted from the original event. Most of the time, these two times will be different."
    )
    loggers: typing.Optional[typing.List[Logger]] = pydantic.Field(
        description="An array of Logger objects that describe the devices and logging products between the event source and its eventual destination. Note, this attribute can be used when there is a complex end-to-end path of event flow."
    )
    modified_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The time when the event was last modified or enriched."
    )
    modified_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The time when the event was last modified or enriched."
    )
    original_time: typing.Optional[str] = pydantic.Field(
        description="The original event time as reported by the event source. For example, the time in the original format from system event log such as Syslog on Unix/Linux and the System event file on Windows. Omit if event is generated instead of collected via logs."
    )
    processed_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The event processed time, such as an ETL operation."
    )
    processed_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The event processed time, such as an ETL operation."
    )
    product: Product = pydantic.Field(description="The product that reported the event.")
    profiles: typing.Optional[typing.List[str]] = pydantic.Field(
        description="The list of profiles used to create the event."
    )
    sequence: typing.Optional[int] = pydantic.Field(
        description="Sequence number of the event. The sequence number is a value available in some events, to make the exact ordering of events unambiguous, regardless of the event time precision."
    )
    tenant_uid: typing.Optional[str] = pydantic.Field(description="The unique tenant identifier.")
    uid: typing.Optional[str] = pydantic.Field(
        description="The logging system-assigned unique identifier of an event instance."
    )
    version: str = pydantic.Field(
        description="The version of the OCSF schema, using Semantic Versioning Specification (<a target='_blank' href='https://semver.org'>SemVer</a>). For example: 1.0.0. Event consumers use the version to determine the available event attributes."
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
