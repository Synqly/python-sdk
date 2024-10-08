# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.hostname import Hostname
from ...base.types.ip_address import IpAddress
from ...base.types.mac_address import MacAddress
from ...base.types.port import Port
from .agent import Agent
from .autonomous_system import AutonomousSystem
from .container import Container
from .device_hw_info import DeviceHwInfo
from .location import Location
from .network_endpoint_type_id import NetworkEndpointTypeId
from .network_proxy import NetworkProxy
from .os import Os
from .user import User

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NetworkEndpoint(pydantic.BaseModel):
    """
    The Network Endpoint object describes characteristics of a network endpoint. These can be a source or destination of a network connection.
    """

    agent_list: typing.Optional[typing.List[Agent]] = pydantic.Field(default=None)
    """
    A list of <code>agent</code> objects associated with a device, endpoint, or resource.
    """

    autonomous_system: typing.Optional[AutonomousSystem] = pydantic.Field(default=None)
    """
    The Autonomous System details associated with an IP address.
    """

    container: typing.Optional[Container] = pydantic.Field(default=None)
    """
    The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the domain.
    """

    hostname: typing.Optional[Hostname] = pydantic.Field(default=None)
    """
    The fully qualified name of the endpoint.
    """

    hw_info: typing.Optional[DeviceHwInfo] = pydantic.Field(default=None)
    """
    The endpoint hardware information.
    """

    instance_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of a VM instance.
    """

    interface_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the network interface (e.g. eth2).
    """

    interface_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the network interface.
    """

    intermediate_ips: typing.Optional[typing.List[IpAddress]] = pydantic.Field(default=None)
    """
    The intermediate IP Addresses. For example, the IP addresses in the HTTP X-Forwarded-For header.
    """

    ip: typing.Optional[IpAddress] = pydantic.Field(default=None)
    """
    The IP address of the endpoint, in either IPv4 or IPv6 format.
    """

    location: typing.Optional[Location] = pydantic.Field(default=None)
    """
    The geographical location of the endpoint.
    """

    mac: typing.Optional[MacAddress] = pydantic.Field(default=None)
    """
    The Media Access Control (MAC) address of the endpoint.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The short name of the endpoint.
    """

    namespace_pid: typing.Optional[int] = pydantic.Field(default=None)
    """
    If running under a process namespace (such as in a container), the process identifier within that process namespace.
    """

    os: typing.Optional[Os] = pydantic.Field(default=None)
    """
    The endpoint operating system.
    """

    owner: typing.Optional[User] = pydantic.Field(default=None)
    """
    The identity of the service or user account that owns the endpoint or was last logged into it.
    """

    port: typing.Optional[Port] = pydantic.Field(default=None)
    """
    The port used for communication within the network connection.
    """

    proxy_endpoint: typing.Optional[NetworkProxy] = pydantic.Field(default=None)
    """
    The network proxy information pertaining to a specific endpoint. This can be used to describe information pertaining to network address translation (NAT).
    """

    subnet_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of a virtual subnet.
    """

    svc_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The service name in service-to-service connections. For example, AWS VPC logs the pkt-src-aws-service and pkt-dst-aws-service fields identify the connection is coming from or going to an AWS service.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The network endpoint type. For example: <code>unknown</code>, <code>server</code>, <code>desktop</code>, <code>laptop</code>, <code>tablet</code>, <code>mobile</code>, <code>virtual</code>, <code>browser</code>, or <code>other</code>.
    """

    type_id: typing.Optional[NetworkEndpointTypeId] = pydantic.Field(default=None)
    """
    The network endpoint type ID.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the endpoint.
    """

    vlan_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Virtual LAN identifier.
    """

    vpc_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Virtual Private Cloud (VPC).
    """

    zone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The network zone or LAN segment.
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
