# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...objects.types.analytic import Analytic
from ...objects.types.api import Api
from ...objects.types.attack import Attack
from ...objects.types.cis_control import CisControl
from ...objects.types.cloud import Cloud
from ...objects.types.compliance import Compliance
from ...objects.types.enrichment import Enrichment
from ...objects.types.finding import Finding
from ...objects.types.kill_chain import KillChain
from ...objects.types.malware import Malware
from ...objects.types.metadata import Metadata
from ...objects.types.object import Object
from ...objects.types.observable import Observable
from ...objects.types.process import Process
from ...objects.types.resource_details import ResourceDetails
from ...objects.types.vulnerability import Vulnerability
from .activity_id import ActivityId
from .category_uid import CategoryUid
from .class_uid import ClassUid
from .confidence_id import ConfidenceId
from .impact_id import ImpactId
from .risk_level_id import RiskLevelId
from .severity_id import SeverityId
from .state_id import StateId
from .status_id import StatusId
from .type_uid import TypeUid

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SecurityFinding(pydantic.BaseModel):
    """
    Security Finding events describe findings, detections, anomalies, alerts and/or actions performed by security products
    """

    activity_id: ActivityId = pydantic.Field()
    """
    The normalized identifier of the activity that triggered the event.
    """

    activity_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event activity name, as defined by the activity_id.
    """

    analytic: typing.Optional[Analytic] = pydantic.Field(default=None)
    """
    The analytic technique used to create the finding or detection
    """

    api: typing.Optional[Api] = pydantic.Field(default=None)
    """
    Describes details about a typical API (Application Programming Interface) call.
    """

    attacks: typing.Optional[typing.List[Attack]] = pydantic.Field(default=None)
    """
    The attack object describes the technique and associated tactics as defined by <a target='_blank' href='https://attack.mitre.org/wiki/ATT&CK_Matrix'>ATT&CK Matrix<sup>TM</sup></a>.
    """

    category_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event category name, as defined by category_uid value: <code>Findings</code>.
    """

    category_uid: CategoryUid = pydantic.Field()
    """
    The category unique identifier of the event.
    """

    cis_csc: typing.Optional[typing.List[CisControl]] = pydantic.Field(default=None)
    """
    The CIS Critical Security Controls is a list of top 20 actions and practices an organization’s security team can take on such that cyber attacks or malware, are minimized and prevented.
    """

    class_uid: ClassUid = pydantic.Field()
    """
    The unique identifier of a class. A Class describes the attributes available in an event.
    """

    cloud: Cloud = pydantic.Field()
    """
    Describes details about the Cloud environment where the event was originally created or logged.
    """

    compliance: typing.Optional[Compliance] = pydantic.Field(default=None)
    """
    The compliance object provides context to compliance findings (e.g., a check against a specific regulatory or best practice framework such as CIS or NIST) and contains compliance related details.
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

    data_sources: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The data sources for the finding.
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

    evidence: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The data the finding exposes to the analyst.
    """

    finding: Finding = pydantic.Field()
    """
    Finding object provides details related to a finding generated by security tool
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

    kill_chain: typing.Optional[typing.List[KillChain]] = pydantic.Field(default=None)
    """
    The <a target='_blank' href='https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html'>Cyber Kill Chain®</a>.
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

    nist: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The NIST Cybersecurity Framework recommendations for managing the cybersecurity risk.
    """

    observables: typing.Optional[typing.List[Observable]] = pydantic.Field(default=None)
    """
    The observables associated with the event.
    """

    process: typing.Optional[Process] = pydantic.Field(default=None)
    """
    The process object.
    """

    raw_data: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event data as received from the event source.
    """

    resources: typing.Optional[typing.List[ResourceDetails]] = pydantic.Field(default=None)
    """
    Describes details about resources that were affected by the activity/event.
    """

    risk_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    The risk level, normalized to the caption of the risk_level_id value. In the case of 'Other', it is defined by the event source.
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

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The normalized state of a security finding.
    """

    state_id: StateId = pydantic.Field()
    """
    The normalized state identifier of a security finding.
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

    vulnerabilities: typing.Optional[typing.List[Vulnerability]] = pydantic.Field(default=None)
    """
    This object describes vulnerabilities reported in a security finding.
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
