# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...objects.types.actor import Actor
from ...objects.types.api import Api
from ...objects.types.cloud import Cloud
from ...objects.types.device import Device
from ...objects.types.enrichment import Enrichment
from ...objects.types.group import Group
from ...objects.types.metadata import Metadata
from ...objects.types.object import Object
from ...objects.types.observable import Observable
from ...objects.types.resource_details import ResourceDetails
from ...objects.types.user import User
from .activity_id import ActivityId
from .category_uid import CategoryUid
from .class_uid import ClassUid
from .severity_id import SeverityId
from .status_id import StatusId
from .type_uid import TypeUid

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GroupManagement(pydantic.BaseModel):
    """
    Group Management events report management updates to a group, including updates to membership and permissions.
    """

    activity_id: ActivityId = pydantic.Field(
        description="The normalized identifier of the activity that triggered the event."
    )
    activity_name: typing.Optional[str] = pydantic.Field(
        description="The event activity name, as defined by the activity_id."
    )
    actor: typing.Optional[Actor] = pydantic.Field(
        description="The actor object describes details about the user/role/process that was the source of the activity."
    )
    api: typing.Optional[Api] = pydantic.Field(
        description="Describes details about a typical API (Application Programming Interface) call."
    )
    category_name: typing.Optional[str] = pydantic.Field(
        description="The event category name, as defined by category_uid value: <code>Identity & Access Management</code>."
    )
    category_uid: CategoryUid = pydantic.Field(description="The category unique identifier of the event.")
    class_uid: ClassUid = pydantic.Field(
        description="The unique identifier of a class. A Class describes the attributes available in an event."
    )
    cloud: Cloud = pydantic.Field(
        description="Describes details about the Cloud environment where the event was originally created or logged."
    )
    count: typing.Optional[int] = pydantic.Field(
        description="The number of times that events in the same logical group occurred during the event <strong>Start Time</strong> to <strong>End Time</strong> period."
    )
    device: typing.Optional[Device] = pydantic.Field(description="An addressable device, computer system or host.")
    duration: typing.Optional[int] = pydantic.Field(
        description="The event duration or aggregate time, the amount of time the event covers from <code>start_time</code> to <code>end_time</code> in milliseconds."
    )
    end_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The end time of a time period, or the time of the most recent event included in the aggregate event."
    )
    end_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The end time of a time period, or the time of the most recent event included in the aggregate event."
    )
    enrichments: typing.Optional[typing.List[Enrichment]] = pydantic.Field(
        description='The additional information from an external data source, which is associated with the event. For example add location information for the IP address in the DNS answers:</p><code>[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]</code>'
    )
    group: Group = pydantic.Field(description="Group that was the target of the event.")
    message: typing.Optional[str] = pydantic.Field(
        description="The description of the event, as defined by the event source."
    )
    metadata: Metadata = pydantic.Field(description="The metadata associated with the event.")
    observables: typing.Optional[typing.List[Observable]] = pydantic.Field(
        description="The observables associated with the event."
    )
    privileges: typing.Optional[typing.List[str]] = pydantic.Field(
        description="A list of privileges assigned to the group."
    )
    raw_data: typing.Optional[str] = pydantic.Field(description="The event data as received from the event source.")
    resource: typing.Optional[ResourceDetails] = pydantic.Field(
        description="Resource that the privileges give access to."
    )
    severity: typing.Optional[str] = pydantic.Field(
        description="The event severity, normalized to the caption of the severity_id value. In the case of 'Other', it is defined by the event source."
    )
    severity_id: SeverityId = pydantic.Field(
        description="<p>The normalized identifier of the event severity.</p>The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events."
    )
    start_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The start time of a time period, or the time of the least recent event included in the aggregate event."
    )
    start_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The start time of a time period, or the time of the least recent event included in the aggregate event."
    )
    status: typing.Optional[str] = pydantic.Field(
        description="The event status, normalized to the caption of the status_id value. In the case of 'Other', it is defined by the event source."
    )
    status_code: typing.Optional[str] = pydantic.Field(
        description="The event status code, as reported by the event source.<br /><br />For example, in a Windows Failed Authentication event, this would be the value of 'Failure Code', e.g. 0x18."
    )
    status_detail: typing.Optional[str] = pydantic.Field(
        description="The status details contains additional information about the event outcome."
    )
    status_id: typing.Optional[StatusId] = pydantic.Field(description="The normalized identifier of the event status.")
    time: Timestamp = pydantic.Field(description="The normalized event occurrence time.")
    time_dt: typing.Optional[dt.datetime] = pydantic.Field(description="The normalized event occurrence time.")
    timezone_offset: typing.Optional[int] = pydantic.Field(
        description="The number of minutes that the reported event <code>time</code> is ahead or behind UTC, in the range -1,080 to +1,080."
    )
    type_name: typing.Optional[str] = pydantic.Field(description="The event type name, as defined by the type_uid.")
    type_uid: TypeUid = pydantic.Field(
        description="The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: <code>class_uid \* 100 + activity_id</code>."
    )
    unmapped: typing.Optional[Object] = pydantic.Field(
        description="The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source."
    )
    user: typing.Optional[User] = pydantic.Field(description="A user that was added to or removed from the group.")

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
