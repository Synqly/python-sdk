# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...objects.types.actor import Actor
from ...objects.types.api import Api
from ...objects.types.attack import Attack
from ...objects.types.cloud import Cloud
from ...objects.types.device import Device
from ...objects.types.enrichment import Enrichment
from ...objects.types.malware import Malware
from ...objects.types.metadata import Metadata
from ...objects.types.module import Module
from ...objects.types.object import Object
from ...objects.types.observable import Observable
from ...objects.types.process import Process
from .activity_id import ActivityId
from .category_uid import CategoryUid
from .class_uid import ClassUid
from .disposition_id import DispositionId
from .injection_type_id import InjectionTypeId
from .severity_id import SeverityId
from .status_id import StatusId
from .type_uid import TypeUid

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProcessActivity(pydantic.BaseModel):
    """
    Process Activity events report when a process launches, injects, opens or terminates another process, successful or otherwise.
    """

    activity_id: ActivityId = pydantic.Field()
    """
    The normalized identifier of the activity that triggered the event.
    """

    activity_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event activity name, as defined by the activity_id.
    """

    actor: Actor = pydantic.Field()
    """
    The actor that performed the activity on the target <code>process</code>. For example, the process that started a new process or injected code into another process.
    """

    actual_permissions: typing.Optional[int] = pydantic.Field(default=None)
    """
    The permissions that were granted to the in a platform-native format.
    """

    api: typing.Optional[Api] = pydantic.Field(default=None)
    """
    Describes details about a typical API (Application Programming Interface) call.
    """

    attacks: typing.Optional[typing.List[Attack]] = pydantic.Field(default=None)
    """
    An array of attacks associated with an event.
    """

    category_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event category name, as defined by category_uid value: <code>System Activity</code>.
    """

    category_uid: CategoryUid = pydantic.Field()
    """
    The category unique identifier of the event.
    """

    class_uid: ClassUid = pydantic.Field()
    """
    The unique identifier of a class. A Class describes the attributes available in an event.
    """

    cloud: Cloud = pydantic.Field()
    """
    Describes details about the Cloud environment where the event was originally created or logged.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of times that events in the same logical group occurred during the event <strong>Start Time</strong> to <strong>End Time</strong> period.
    """

    device: Device = pydantic.Field()
    """
    An addressable device, computer system or host.
    """

    disposition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event disposition name, normalized to the caption of the disposition_id value. In the case of 'Other', it is defined by the event source.
    """

    disposition_id: DispositionId = pydantic.Field()
    """
    When security issues, such as malware or policy violations, are detected and possibly corrected, then <code>disposition_id</code> describes the action taken by the security product.
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The event duration or aggregate time, the amount of time the event covers from <code>start_time</code> to <code>end_time</code> in milliseconds.
    """

    end_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The end time of a time period, or the time of the most recent event included in the aggregate event.
    """

    end_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The end time of a time period, or the time of the most recent event included in the aggregate event.
    """

    enrichments: typing.Optional[typing.List[Enrichment]] = pydantic.Field(default=None)
    """
    The additional information from an external data source, which is associated with the event. For example add location information for the IP address in the DNS answers:</p><code>[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]</code>
    """

    exit_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    The exit code reported by a process when it terminates. The convention is that zero indicates success and any non-zero exit code indicates that some error occurred.
    """

    injection_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The process injection method, normalized to the caption of the injection_type_id value. In the case of 'Other', it is defined by the event source.
    """

    injection_type_id: typing.Optional[InjectionTypeId] = pydantic.Field(default=None)
    """
    The normalized identifier of the process injection method.
    """

    malware: typing.Optional[typing.List[Malware]] = pydantic.Field(default=None)
    """
    The list of malware identified by a finding.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the event, as defined by the event source.
    """

    metadata: Metadata = pydantic.Field()
    """
    The metadata associated with the event.
    """

    module: typing.Optional[Module] = pydantic.Field(default=None)
    """
    The module that was injected by the actor process.
    """

    observables: typing.Optional[typing.List[Observable]] = pydantic.Field(default=None)
    """
    The observables associated with the event.
    """

    process: Process = pydantic.Field()
    """
    The process that was launched, injected into, opened, or terminated.
    """

    raw_data: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event data as received from the event source.
    """

    requested_permissions: typing.Optional[int] = pydantic.Field(default=None)
    """
    The permissions mask that were requested by the process.
    """

    severity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event severity, normalized to the caption of the severity_id value. In the case of 'Other', it is defined by the event source.
    """

    severity_id: SeverityId = pydantic.Field()
    """
    <p>The normalized identifier of the event severity.</p>The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events.
    """

    start_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The start time of a time period, or the time of the least recent event included in the aggregate event.
    """

    start_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The start time of a time period, or the time of the least recent event included in the aggregate event.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event status, normalized to the caption of the status_id value. In the case of 'Other', it is defined by the event source.
    """

    status_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event status code, as reported by the event source.<br /><br />For example, in a Windows Failed Authentication event, this would be the value of 'Failure Code', e.g. 0x18.
    """

    status_detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status details contains additional information about the event outcome.
    """

    status_id: typing.Optional[StatusId] = pydantic.Field(default=None)
    """
    The normalized identifier of the event status.
    """

    time: Timestamp = pydantic.Field()
    """
    The normalized event occurrence time.
    """

    time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The normalized event occurrence time.
    """

    timezone_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of minutes that the reported event <code>time</code> is ahead or behind UTC, in the range -1,080 to +1,080.
    """

    type_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event type name, as defined by the type_uid.
    """

    type_uid: TypeUid = pydantic.Field()
    """
    The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: <code>class_uid \* 100 + activity_id</code>.
    """

    unmapped: typing.Optional[Object] = pydantic.Field(default=None)
    """
    The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.
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
