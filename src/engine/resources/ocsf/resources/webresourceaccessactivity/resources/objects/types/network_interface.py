# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime
from ...base.types.hostname import Hostname
from ...base.types.ip_address import IpAddress
from ...base.types.mac_address import MacAddress
from .network_interface_type_id import NetworkInterfaceTypeId


class NetworkInterface(pydantic.BaseModel):
    """
    The Network Interface object describes the type and associated addresses of a network interface.
    """

    hostname: typing.Optional[Hostname] = pydantic.Field(
        description="The hostname associated with the network interface."
    )
    ip: typing.Optional[IpAddress] = pydantic.Field(description="The IP address associated with the network interface.")
    mac: typing.Optional[MacAddress] = pydantic.Field(description="The MAC address of the network interface.")
    name: typing.Optional[str] = pydantic.Field(description="The name of the network interface.")
    namespace: typing.Optional[str] = pydantic.Field(
        description="The namespace is useful in merger or acquisition situations. For example, when similar entities exists that you need to keep separate."
    )
    type: typing.Optional[str] = pydantic.Field(description="The type of network interface.")
    type_id: NetworkInterfaceTypeId = pydantic.Field(description="The network interface type identifier.")
    uid: typing.Optional[str] = pydantic.Field(description="The unique identifier for the network interface.")

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