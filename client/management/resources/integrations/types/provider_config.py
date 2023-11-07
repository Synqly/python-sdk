# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .event_config import EventConfig
from .hooks_config import HooksConfig
from .identity_config import IdentityConfig
from .notification_config import NotificationConfig
from .storage_config import StorageConfig
from .ticket_config import TicketConfig
from .vulnerability_config import VulnerabilityConfig


class ProviderConfig_Events(EventConfig):
    type: typing_extensions.Literal["events"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_Hooks(HooksConfig):
    type: typing_extensions.Literal["hooks"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_Identity(IdentityConfig):
    type: typing_extensions.Literal["identity"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_Notifications(NotificationConfig):
    type: typing_extensions.Literal["notifications"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_Storage(StorageConfig):
    type: typing_extensions.Literal["storage"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_Tickets(TicketConfig):
    type: typing_extensions.Literal["tickets"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_Vulnerabilities(VulnerabilityConfig):
    type: typing_extensions.Literal["vulnerabilities"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ProviderConfig = typing.Union[
    ProviderConfig_Events,
    ProviderConfig_Hooks,
    ProviderConfig_Identity,
    ProviderConfig_Notifications,
    ProviderConfig_Storage,
    ProviderConfig_Tickets,
    ProviderConfig_Vulnerabilities,
]
