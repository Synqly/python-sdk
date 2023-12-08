# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ...ocsf.resources.accountchange.resources.classes.types.account_change import AccountChange
from ...ocsf.resources.apiactivity.resources.classes.types.api_activity import ApiActivity
from ...ocsf.resources.authentication.resources.classes.types.authentication import Authentication
from ...ocsf.resources.fileactivity.resources.classes.types.file_activity import FileActivity
from ...ocsf.resources.groupmanagement.resources.classes.types.group_management import GroupManagement
from ...ocsf.resources.inventoryinfo.resources.classes.types.inventory_info import InventoryInfo
from ...ocsf.resources.networkactivity.resources.classes.types.network_activity import NetworkActivity
from ...ocsf.resources.processactivity.resources.classes.types.process_activity import ProcessActivity
from ...ocsf.resources.scheduledjobactivity.resources.classes.types.scheduled_job_activity import ScheduledJobActivity
from ...ocsf.resources.securityfinding.resources.classes.types.security_finding import SecurityFinding
from ...ocsf.resources.webresourceaccessactivity.resources.classes.types.web_resource_access_activity import (
    WebResourceAccessActivity,
)


class Event_AccountChange(AccountChange):
    class_name: typing_extensions.Literal["Account Change"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ApiActivity(ApiActivity):
    class_name: typing_extensions.Literal["Api Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_Authentication(Authentication):
    class_name: typing_extensions.Literal["Authentication"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_FileActivity(FileActivity):
    class_name: typing_extensions.Literal["File Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_GroupManagement(GroupManagement):
    class_name: typing_extensions.Literal["Group Management"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_DeviceInventoryInfo(InventoryInfo):
    class_name: typing_extensions.Literal["Device Inventory Info"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_NetworkActivity(NetworkActivity):
    class_name: typing_extensions.Literal["Network Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ProcessActivity(ProcessActivity):
    class_name: typing_extensions.Literal["Process Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_ScheduledJobActivity(ScheduledJobActivity):
    class_name: typing_extensions.Literal["Scheduled Job Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SecurityFinding(SecurityFinding):
    class_name: typing_extensions.Literal["Security Finding"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_WebResourceAccessActivity(WebResourceAccessActivity):
    class_name: typing_extensions.Literal["Web Resource Access Activity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


Event = typing.Union[
    Event_AccountChange,
    Event_ApiActivity,
    Event_Authentication,
    Event_FileActivity,
    Event_GroupManagement,
    Event_DeviceInventoryInfo,
    Event_NetworkActivity,
    Event_ProcessActivity,
    Event_ScheduledJobActivity,
    Event_SecurityFinding,
    Event_WebResourceAccessActivity,
]
