# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.hostname import Hostname
from ...base.types.ip_address import IpAddress
from ...base.types.mac_address import MacAddress
from ...base.types.port import Port
from .location import Location

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NetworkEndpoint(pydantic.BaseModel):
    """
    The Network Endpoint object describes characteristics of a network endpoint. These can be a source or destination of a network connection.
    """

    domain: typing.Optional[str] = pydantic.Field(description="The name of the domain.")
    hostname: typing.Optional[Hostname] = pydantic.Field(description="The fully qualified name of the endpoint.")
    instance_uid: typing.Optional[str] = pydantic.Field(description="The unique identifier of a VM instance.")
    interface_name: typing.Optional[str] = pydantic.Field(description="The name of the network interface (e.g. eth2).")
    interface_uid: typing.Optional[str] = pydantic.Field(description="The unique identifier of the network interface.")
    intermediate_ips: typing.Optional[typing.List[IpAddress]] = pydantic.Field(
        description="The intermediate IP Addresses. For example, the IP addresses in the HTTP X-Forwarded-For header."
    )
    ip: typing.Optional[IpAddress] = pydantic.Field(
        description="The IP address of the endpoint, in either IPv4 or IPv6 format."
    )
    location: typing.Optional[Location] = pydantic.Field(description="The geographical location of the endpoint.")
    mac: typing.Optional[MacAddress] = pydantic.Field(
        description="The Media Access Control (MAC) address of the endpoint."
    )
    name: typing.Optional[str] = pydantic.Field(description="The short name of the endpoint.")
    port: typing.Optional[Port] = pydantic.Field(
        description="The port used for communication within the network connection."
    )
    subnet_uid: typing.Optional[str] = pydantic.Field(description="The unique identifier of a virtual subnet.")
    svc_name: typing.Optional[str] = pydantic.Field(
        description="The service name in service-to-service connections. For example, AWS VPC logs the pkt-src-aws-service and pkt-dst-aws-service fields identify the connection is coming from or going to an AWS service."
    )
    uid: typing.Optional[str] = pydantic.Field(description="The unique identifier of the endpoint.")
    vlan_uid: typing.Optional[str] = pydantic.Field(description="The Virtual LAN identifier.")
    vpc_uid: typing.Optional[str] = pydantic.Field(
        description="The unique identifier of the Virtual Private Cloud (VPC)."
    )

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
