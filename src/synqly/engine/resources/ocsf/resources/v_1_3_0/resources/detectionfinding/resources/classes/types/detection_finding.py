# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...objects.types.actor import Actor
from ...objects.types.api import Api
from ...objects.types.attack import Attack
from ...objects.types.authorization import Authorization
from ...objects.types.cloud import Cloud
from ...objects.types.device import Device
from ...objects.types.enrichment import Enrichment
from ...objects.types.evidences import Evidences
from ...objects.types.finding_info import FindingInfo
from ...objects.types.firewall_rule import FirewallRule
from ...objects.types.malware import Malware
from ...objects.types.metadata import Metadata
from ...objects.types.object import Object
from ...objects.types.observable import Observable
from ...objects.types.remediation import Remediation
from ...objects.types.resource_details import ResourceDetails
from ...objects.types.vulnerability import Vulnerability
from .action_id import ActionId
from .activity_id import ActivityId
from .category_uid import CategoryUid
from .class_uid import ClassUid
from .confidence_id import ConfidenceId
from .disposition_id import DispositionId
from .impact_id import ImpactId
from .risk_level_id import RiskLevelId
from .severity_id import SeverityId
from .status_id import StatusId
from .type_uid import TypeUid

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DetectionFinding(pydantic.BaseModel):
    """
    A Detection Finding describes detections or alerts generated by security products using correlation engines, detection engines or other methodologies. Note: if the product is a security control, the <code>security_control</code> profile should be applied and its <code>attacks</code> information should be duplicated into the <code>finding_info</code> object.
    """

    action: typing.Optional[str] = pydantic.Field(default=None)
    """
    The normalized caption of <code>action_id</code>.
    """

    action_id: ActionId = pydantic.Field()
    """
    The action taken by a control or other policy-based system leading to an outcome or disposition. Dispositions conform to an action of <code>1</code> 'Allowed' or <code>2</code> 'Denied' in most cases. Note that <code>99</code> 'Other' is not an option. No action would equate to <code>1</code> 'Allowed'. An unknown action may still correspond to a known disposition. Refer to <code>disposition_id</code> for the outcome of the action.
    """

    activity_id: ActivityId = pydantic.Field()
    """
    The normalized identifier of the finding activity.
    """

    activity_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The finding activity name, as defined by the <code>activity_id</code>.
    """

    actor: typing.Optional[Actor] = pydantic.Field(default=None)
    """
    The actor object describes details about the user/role/process that was the source of the activity.
    """

    api: typing.Optional[Api] = pydantic.Field(default=None)
    """
    Describes details about a typical API (Application Programming Interface) call.
    """

    attacks: typing.Optional[typing.List[Attack]] = pydantic.Field(default=None)
    """
    An array of <a target='_blank' href='https://attack.mitre.org'>MITRE ATT&CK®</a> objects describing the tactics, techniques & sub-techniques identified by a security control or finding.
    """

    authorizations: typing.Optional[typing.List[Authorization]] = pydantic.Field(default=None)
    """
    Provides details about an authorization, such as authorization outcome, and any associated policies related to the activity/event.
    """

    category_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event category name, as defined by category_uid value: <code>Findings</code>.
    """

    category_uid: CategoryUid = pydantic.Field()
    """
    The category unique identifier of the event.
    """

    class_uid: ClassUid = pydantic.Field()
    """
    The unique identifier of a class. A class describes the attributes available in an event.
    """

    cloud: typing.Optional[Cloud] = pydantic.Field(default=None)
    """
    Describes details about the Cloud environment where the event was originally created or logged.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    A user provided comment about the finding.
    """

    confidence: typing.Optional[str] = pydantic.Field(default=None)
    """
    The confidence, normalized to the caption of the confidence_id value. In the case of 'Other', it is defined by the event source.
    """

    confidence_id: typing.Optional[ConfidenceId] = pydantic.Field(default=None)
    """
    The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.
    """

    confidence_score: typing.Optional[int] = pydantic.Field(default=None)
    """
    The confidence score as reported by the event source.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of times that events in the same logical group occurred during the event <strong>Start Time</strong> to <strong>End Time</strong> period.
    """

    device: typing.Optional[Device] = pydantic.Field(default=None)
    """
    Describes the affected device/host. It can be used in conjunction with <code>Affected Resource(s)</code>. <p> e.g. Specific details about an AWS EC2 instance, that is affected by the Finding.</p>
    """

    disposition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The disposition name, normalized to the caption of the disposition_id value. In the case of 'Other', it is defined by the event source.
    """

    disposition_id: typing.Optional[DispositionId] = pydantic.Field(default=None)
    """
    Describes the outcome or action taken by a security control, such as access control checks, malware detections or various types of policy violations.
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The event duration or aggregate time, the amount of time the event covers from <code>start_time</code> to <code>end_time</code> in milliseconds.
    """

    end_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time of the most recent event included in the finding.
    """

    end_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time of the most recent event included in the finding.
    """

    enrichments: typing.Optional[typing.List[Enrichment]] = pydantic.Field(default=None)
    """
    The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:</p><code>[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]</code>
    """

    evidences: typing.Optional[typing.List[Evidences]] = pydantic.Field(default=None)
    """
    Describes various evidence artifacts associated to the activity/activities that triggered a security detection.
    """

    finding_info: FindingInfo = pydantic.Field()
    """
    Describes the supporting information about a generated finding.
    """

    firewall_rule: typing.Optional[FirewallRule] = pydantic.Field(default=None)
    """
    The firewall rule that triggered the event.
    """

    impact: typing.Optional[str] = pydantic.Field(default=None)
    """
    The impact , normalized to the caption of the impact_id value. In the case of 'Other', it is defined by the event source.
    """

    impact_id: typing.Optional[ImpactId] = pydantic.Field(default=None)
    """
    The normalized impact of the finding.
    """

    impact_score: typing.Optional[int] = pydantic.Field(default=None)
    """
    The impact of the finding, valid range 0-100.
    """

    malware: typing.Optional[typing.List[Malware]] = pydantic.Field(default=None)
    """
    A list of Malware objects, describing details about the identified malware.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the event/finding, as defined by the source.
    """

    metadata: Metadata = pydantic.Field()
    """
    The metadata associated with the event or a finding.
    """

    observables: typing.Optional[typing.List[Observable]] = pydantic.Field(default=None)
    """
    The observables associated with the event or a finding.
    """

    raw_data: typing.Optional[str] = pydantic.Field(default=None)
    """
    The raw event/finding data as received from the source.
    """

    remediation: typing.Optional[Remediation] = pydantic.Field(default=None)
    """
    Describes the recommended remediation steps to address identified issue(s).
    """

    resources: typing.Optional[typing.List[ResourceDetails]] = pydantic.Field(default=None)
    """
    Describes details about resources that were the target of the activity that triggered the finding.
    """

    risk_details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Describes the risk associated with the finding.
    """

    risk_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    The risk level, normalized to the caption of the risk_level_id value.
    """

    risk_level_id: typing.Optional[RiskLevelId] = pydantic.Field(default=None)
    """
    The normalized risk level id.
    """

    risk_score: typing.Optional[int] = pydantic.Field(default=None)
    """
    The risk score as reported by the event source.
    """

    severity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event/finding severity, normalized to the caption of the severity_id value. In the case of 'Other', it is defined by the source.
    """

    severity_id: SeverityId = pydantic.Field()
    """
    <p>The normalized identifier of the event/finding severity.</p>The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events.
    """

    start_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time of the least recent event included in the finding.
    """

    start_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time of the least recent event included in the finding.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The normalized status of the Finding set by the consumer normalized to the caption of the status_id value. In the case of 'Other', it is defined by the source.
    """

    status_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event status code, as reported by the event source.<br /><br />For example, in a Windows Failed Authentication event, this would be the value of 'Failure Code', e.g. 0x18.
    """

    status_detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status detail contains additional information about the event/finding outcome.
    """

    status_id: typing.Optional[StatusId] = pydantic.Field(default=None)
    """
    The normalized status identifier of the Finding, set by the consumer.
    """

    time: Timestamp = pydantic.Field()
    """
    The normalized event occurrence time or the finding creation time.
    """

    time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The normalized event occurrence time or the finding creation time.
    """

    timezone_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of minutes that the reported event <code>time</code> is ahead or behind UTC, in the range -1,080 to +1,080.
    """

    type_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event/finding type name, as defined by the type_uid.
    """

    type_uid: TypeUid = pydantic.Field()
    """
    The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: <code>class_uid \* 100 + activity_id</code>.
    """

    unmapped: typing.Optional[Object] = pydantic.Field(default=None)
    """
    The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.
    """

    vulnerabilities: typing.Optional[typing.List[Vulnerability]] = pydantic.Field(default=None)
    """
    Describes vulnerabilities reported in a Detection Finding.
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
