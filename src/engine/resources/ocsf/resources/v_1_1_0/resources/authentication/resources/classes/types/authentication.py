# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...objects.types.actor import Actor
from ...objects.types.api import Api
from ...objects.types.certificate import Certificate
from ...objects.types.cloud import Cloud
from ...objects.types.device import Device
from ...objects.types.enrichment import Enrichment
from ...objects.types.http_request import HttpRequest
from ...objects.types.metadata import Metadata
from ...objects.types.network_endpoint import NetworkEndpoint
from ...objects.types.object import Object
from ...objects.types.observable import Observable
from ...objects.types.process import Process
from ...objects.types.service import Service
from ...objects.types.session import Session
from ...objects.types.user import User
from .activity_id import ActivityId
from .auth_protocol_id import AuthProtocolId
from .category_uid import CategoryUid
from .class_uid import ClassUid
from .logon_type_id import LogonTypeId
from .severity_id import SeverityId
from .status_id import StatusId
from .type_uid import TypeUid

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Authentication(pydantic.BaseModel):
    """
    Authentication events report authentication session activities such as user attempts a logon or logoff, successfully or otherwise.
    """

    activity_id: ActivityId = pydantic.Field(
        description="The normalized identifier of the activity that triggered the event."
    )
    activity_name: typing.Optional[str] = pydantic.Field(
        description="The event activity name, as defined by the activity_id."
    )
    actor: typing.Optional[Actor] = pydantic.Field(description="The actor that requested the authentication.")
    api: typing.Optional[Api] = pydantic.Field(
        description="Describes details about a typical API (Application Programming Interface) call."
    )
    auth_protocol: typing.Optional[str] = pydantic.Field(
        description="The authentication protocol as defined by the caption of 'auth_protocol_id'. In the case of 'Other', it is defined by the event source."
    )
    auth_protocol_id: typing.Optional[AuthProtocolId] = pydantic.Field(
        description="The normalized identifier of the authentication protocol used to create the user session."
    )
    category_name: typing.Optional[str] = pydantic.Field(
        description="The event category name, as defined by category_uid value: <code>Identity & Access Management</code>."
    )
    category_uid: CategoryUid = pydantic.Field(description="The category unique identifier of the event.")
    certificate: typing.Optional[Certificate] = pydantic.Field(
        description="The certificate associated with the authentication or pre-authentication (Kerberos)."
    )
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
    dst_endpoint: typing.Optional[NetworkEndpoint] = pydantic.Field(
        description="The endpoint to which the authentication was targeted."
    )
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
        description='The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:</p><code>[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]</code>'
    )
    http_request: typing.Optional[HttpRequest] = pydantic.Field(
        description="Details about the underlying http request."
    )
    is_cleartext: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether the credentials were passed in clear text.<p><b>Note:</b> True if the credentials were passed in a clear text protocol such as FTP or TELNET, or if Windows detected that a user's logon password was passed to the authentication package in clear text.</p>"
    )
    is_mfa: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether Multi Factor Authentication was used during authentication."
    )
    is_new_logon: typing.Optional[bool] = pydantic.Field(
        description="Indicates logon is from a device not seen before or a first time account logon."
    )
    is_remote: typing.Optional[bool] = pydantic.Field(
        description="The attempted authentication is over a remote connection."
    )
    logon_process: typing.Optional[Process] = pydantic.Field(
        description="The trusted process that validated the authentication credentials."
    )
    logon_type: typing.Optional[str] = pydantic.Field(
        description="The logon type, normalized to the caption of the logon_type_id value. In the case of 'Other', it is defined by the event source."
    )
    logon_type_id: typing.Optional[LogonTypeId] = pydantic.Field(description="The normalized logon type identifier.")
    message: typing.Optional[str] = pydantic.Field(
        description="The description of the event/finding, as defined by the source."
    )
    metadata: Metadata = pydantic.Field(description="The metadata associated with the event or a finding.")
    observables: typing.Optional[typing.List[Observable]] = pydantic.Field(
        description="The observables associated with the event or a finding."
    )
    raw_data: typing.Optional[str] = pydantic.Field(
        description="The raw event/finding data as received from the source."
    )
    service: typing.Optional[Service] = pydantic.Field(
        description="The service or gateway to which the user or process is being authenticated"
    )
    session: typing.Optional[Session] = pydantic.Field(description="The authenticated user or service session.")
    severity: typing.Optional[str] = pydantic.Field(
        description="The event/finding severity, normalized to the caption of the severity_id value. In the case of 'Other', it is defined by the source."
    )
    severity_id: SeverityId = pydantic.Field(
        description="<p>The normalized identifier of the event/finding severity.</p>The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events."
    )
    src_endpoint: typing.Optional[NetworkEndpoint] = pydantic.Field(
        description="The Endpoint from which the authentication was requested."
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
        description="The details about the authentication request. For example, possible details for Windows logon or logoff events are:<ul><li>Success</li><ul><li>LOGOFF_USER_INITIATED</li><li>LOGOFF_OTHER</li></ul><li>Failure</li><ul><li>USER_DOES_NOT_EXIST</li><li>INVALID_CREDENTIALS</li><li>ACCOUNT_DISABLED</li><li>ACCOUNT_LOCKED_OUT</li><li>PASSWORD_EXPIRED</li></ul></ul>"
    )
    status_id: typing.Optional[StatusId] = pydantic.Field(description="The normalized identifier of the event status.")
    time: Timestamp = pydantic.Field(description="The normalized event occurrence time or the finding creation time.")
    time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The normalized event occurrence time or the finding creation time."
    )
    timezone_offset: typing.Optional[int] = pydantic.Field(
        description="The number of minutes that the reported event <code>time</code> is ahead or behind UTC, in the range -1,080 to +1,080."
    )
    type_name: typing.Optional[str] = pydantic.Field(
        description="The event/finding type name, as defined by the type_uid."
    )
    type_uid: TypeUid = pydantic.Field(
        description="The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: <code>class_uid \* 100 + activity_id</code>."
    )
    unmapped: typing.Optional[Object] = pydantic.Field(
        description="The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source."
    )
    user: User = pydantic.Field(description="The subject (user/role or account) to authenticate.")

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
