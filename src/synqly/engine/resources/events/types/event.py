# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...ocsf.resources.v_1_1_0.resources.accountchange.resources.classes.types.account_change import AccountChange
from ...ocsf.resources.v_1_1_0.resources.apiactivity.resources.classes.types.api_activity import ApiActivity
from ...ocsf.resources.v_1_1_0.resources.authentication.resources.classes.types.authentication import Authentication
from ...ocsf.resources.v_1_1_0.resources.compliancefinding.resources.classes.types.compliance_finding import (
    ComplianceFinding,
)
from ...ocsf.resources.v_1_1_0.resources.fileactivity.resources.classes.types.file_activity import FileActivity
from ...ocsf.resources.v_1_1_0.resources.groupmanagement.resources.classes.types.group_management import GroupManagement
from ...ocsf.resources.v_1_1_0.resources.moduleactivity.resources.classes.types.module_activity import ModuleActivity
from ...ocsf.resources.v_1_1_0.resources.networkactivity.resources.classes.types.network_activity import NetworkActivity
from ...ocsf.resources.v_1_1_0.resources.processactivity.resources.classes.types.process_activity import ProcessActivity
from ...ocsf.resources.v_1_1_0.resources.scheduledjobactivity.resources.classes.types.scheduled_job_activity import (
    ScheduledJobActivity,
)
from ...ocsf.resources.v_1_1_0.resources.securityfinding.resources.classes.types.security_finding import SecurityFinding
from ...ocsf.resources.v_1_1_0.resources.webresourceaccessactivity.resources.classes.types.web_resource_access_activity import (
    WebResourceAccessActivity,
)
from ...ocsf.resources.v_1_3_0.resources.authorizesession.resources.classes.types.authorize_session import (
    AuthorizeSession,
)
from ...ocsf.resources.v_1_3_0.resources.baseevent.resources.classes.types.base_event import BaseEvent
from ...ocsf.resources.v_1_3_0.resources.configstate.resources.classes.types.config_state import ConfigState
from ...ocsf.resources.v_1_3_0.resources.detectionfinding.resources.classes.types.detection_finding import (
    DetectionFinding,
)
from ...ocsf.resources.v_1_3_0.resources.incidentfinding.resources.classes.types.incident_finding import IncidentFinding
from ...ocsf.resources.v_1_3_0.resources.inventoryinfo.resources.classes.types.inventory_info import InventoryInfo
from ...ocsf.resources.v_1_3_0.resources.scanactivity.resources.classes.types.scan_activity import ScanActivity
from ...ocsf.resources.v_1_3_0.resources.softwareinfo.resources.classes.types.software_info import SoftwareInfo
from ...ocsf.resources.v_1_3_0.resources.useraccessmanagement.resources.classes.types.user_access import UserAccess
from ...ocsf.resources.v_1_3_0.resources.vulnerabilityfinding.resources.classes.types.vulnerability_finding import (
    VulnerabilityFinding,
)


class Event_AccountChange(AccountChange):
    class_name: typing.Literal["Account Change"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ApiActivity(ApiActivity):
    class_name: typing.Literal["API Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_Authentication(Authentication):
    class_name: typing.Literal["Authentication"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_AuthorizeSession(AuthorizeSession):
    class_name: typing.Literal["Authorize Session"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_BaseEvent(BaseEvent):
    class_name: typing.Literal["Base Event"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ComplianceFinding(ComplianceFinding):
    class_name: typing.Literal["Compliance Finding"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_DeviceConfigState(ConfigState):
    class_name: typing.Literal["Device Config State"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_DetectionFinding(DetectionFinding):
    class_name: typing.Literal["Detection Finding"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_FileSystemActivity(FileActivity):
    class_name: typing.Literal["File System Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_GroupManagement(GroupManagement):
    class_name: typing.Literal["Group Management"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_IncidentFinding(IncidentFinding):
    class_name: typing.Literal["Incident Finding"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_DeviceInventoryInfo(InventoryInfo):
    class_name: typing.Literal["Device Inventory Info"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ModuleActivity(ModuleActivity):
    class_name: typing.Literal["Module Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_NetworkActivity(NetworkActivity):
    class_name: typing.Literal["Network Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ProcessActivity(ProcessActivity):
    class_name: typing.Literal["Process Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ScanActivity(ScanActivity):
    class_name: typing.Literal["Scan Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ScheduledJobActivity(ScheduledJobActivity):
    class_name: typing.Literal["Scheduled Job Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SecurityFinding(SecurityFinding):
    class_name: typing.Literal["Security Finding"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SoftwareInfo(SoftwareInfo):
    class_name: typing.Literal["Software Info"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_UserAccessManagement(UserAccess):
    class_name: typing.Literal["User Access Management"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_VulnerabilityFinding(VulnerabilityFinding):
    class_name: typing.Literal["Vulnerability Finding"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_WebResourceAccessActivity(WebResourceAccessActivity):
    class_name: typing.Literal["Web Resource Access Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


Event = typing.Union[
    Event_AccountChange,
    Event_ApiActivity,
    Event_Authentication,
    Event_AuthorizeSession,
    Event_BaseEvent,
    Event_ComplianceFinding,
    Event_DeviceConfigState,
    Event_DetectionFinding,
    Event_FileSystemActivity,
    Event_GroupManagement,
    Event_IncidentFinding,
    Event_DeviceInventoryInfo,
    Event_ModuleActivity,
    Event_NetworkActivity,
    Event_ProcessActivity,
    Event_ScanActivity,
    Event_ScheduledJobActivity,
    Event_SecurityFinding,
    Event_SoftwareInfo,
    Event_UserAccessManagement,
    Event_VulnerabilityFinding,
    Event_WebResourceAccessActivity,
]
