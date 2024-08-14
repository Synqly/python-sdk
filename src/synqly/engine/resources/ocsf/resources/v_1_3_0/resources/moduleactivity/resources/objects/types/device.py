# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.hostname import Hostname
from ...base.types.ip_address import IpAddress
from ...base.types.mac_address import MacAddress
from ...base.types.subnet import Subnet
from ...base.types.timestamp import Timestamp
from .agent import Agent
from .container import Container
from .device_hw_info import DeviceHwInfo
from .device_risk_level_id import DeviceRiskLevelId
from .device_type_id import DeviceTypeId
from .group import Group
from .image import Image
from .location import Location
from .network_interface import NetworkInterface
from .organization import Organization
from .os import Os
from .product import Product
from .user import User

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Device(pydantic.BaseModel):
    """
    The Device object represents an addressable computer system or host, which is typically connected to a computer network and participates in the transmission or processing of data within the computer network. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:Host/'>d3f:Host</a>.
    """

    agent_list: typing.Optional[typing.List[Agent]] = pydantic.Field(default=None)
    """
    A list of <code>agent</code> objects associated with a device, endpoint, or resource.
    """

    autoscale_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the cloud autoscale configuration.
    """

    boot_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time the system was booted.
    """

    boot_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time the system was booted.
    """

    container: typing.Optional[Container] = pydantic.Field(default=None)
    """
    The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the device was known to have been created.
    """

    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the device was known to have been created.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the device, ordinarily as reported by the operating system.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The network domain where the device resides. For example: <code>work.example.com</code>.
    """

    first_seen_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The initial discovery time of the device.
    """

    first_seen_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The initial discovery time of the device.
    """

    groups: typing.Optional[typing.List[Group]] = pydantic.Field(default=None)
    """
    The group names to which the device belongs. For example: <code>["Windows Laptops", "Engineering"]<code/>.
    """

    hostname: typing.Optional[Hostname] = pydantic.Field(default=None)
    """
    The device hostname.
    """

    hw_info: typing.Optional[DeviceHwInfo] = pydantic.Field(default=None)
    """
    The endpoint hardware information.
    """

    hypervisor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the hypervisor running on the device. For example, <code>Xen</code>, <code>VMware</code>, <code>Hyper-V</code>, <code>VirtualBox</code>, etc.
    """

    image: typing.Optional[Image] = pydantic.Field(default=None)
    """
    The image used as a template to run the virtual machine.
    """

    imei: typing.Optional[str] = pydantic.Field(default=None)
    """
    The International Mobile Station Equipment Identifier that is associated with the device.
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

    ip: typing.Optional[IpAddress] = pydantic.Field(default=None)
    """
    The device IP address, in either IPv4 or IPv6 format.
    """

    ip_addresses: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of IP addresses available on the device
    """

    is_compliant: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The event occurred on a compliant device.
    """

    is_managed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The event occurred on a managed device.
    """

    is_personal: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The event occurred on a personal device.
    """

    is_trusted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The event occurred on a trusted device.
    """

    last_seen_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The most recent discovery time of the device.
    """

    last_seen_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The most recent discovery time of the device.
    """

    location: typing.Optional[Location] = pydantic.Field(default=None)
    """
    The geographical location of the device.
    """

    mac: typing.Optional[MacAddress] = pydantic.Field(default=None)
    """
    The Media Access Control (MAC) address of the endpoint.
    """

    mac_addresses: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of MAC addresses available on the device
    """

    modified_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the device was last known to have been modified.
    """

    modified_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the device was last known to have been modified.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The alternate device name, ordinarily as assigned by an administrator. <p><b>Note:</b> The <b>Name</b> could be any other string that helps to identify the device, such as a phone number; for example <code>310-555-1234</code>.</p>
    """

    namespace_pid: typing.Optional[int] = pydantic.Field(default=None)
    """
    If running under a process namespace (such as in a container), the process identifier within that process namespace.
    """

    netbios_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of NetBIOS names available on the device
    """

    network_interfaces: typing.Optional[typing.List[NetworkInterface]] = pydantic.Field(default=None)
    """
    The network interfaces that are associated with the device, one for each unique MAC address/IP address/hostname/name combination.<p><b>Note:</b> The first element of the array is the network information that pertains to the event.</p>
    """

    org: typing.Optional[Organization] = pydantic.Field(default=None)
    """
    Organization and org unit related to the device.
    """

    os: typing.Optional[Os] = pydantic.Field(default=None)
    """
    The endpoint operating system.
    """

    owner: typing.Optional[User] = pydantic.Field(default=None)
    """
    The identity of the service or user account that owns the endpoint or was last logged into it.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region where the virtual machine is located. For example, an AWS Region.
    """

    risk_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    The risk level, normalized to the caption of the risk_level_id value.
    """

    risk_level_id: typing.Optional[DeviceRiskLevelId] = pydantic.Field(default=None)
    """
    The normalized risk level id.
    """

    risk_score: typing.Optional[int] = pydantic.Field(default=None)
    """
    The risk score as reported by the event source.
    """

    subnet: typing.Optional[Subnet] = pydantic.Field(default=None)
    """
    The subnet mask.
    """

    subnet_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of a virtual subnet.
    """

    sw_info: typing.Optional[typing.List[Product]] = pydantic.Field(default=None)
    """
    The list of software contained on a device
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The device type. For example: <code>unknown</code>, <code>server</code>, <code>desktop</code>, <code>laptop</code>, <code>tablet</code>, <code>mobile</code>, <code>virtual</code>, <code>browser</code>, <code>plc</code>, <code>scada</code>, <code>dcs</code>, <code>cnc</code>, <code>scientific</code>, <code>medical</code>, <code>lighting</code>, <code>energy</code>, <code>transportation</code> <code>other</code>.
    """

    type_id: DeviceTypeId = pydantic.Field()
    """
    The device type ID.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the device. For example the Windows TargetSID or AWS EC2 ARN.
    """

    uid_alt: typing.Optional[str] = pydantic.Field(default=None)
    """
    An alternate unique identifier of the device if any. For example the ActiveDirectory DN.
    """

    vendor: typing.Optional[Organization] = pydantic.Field(default=None)
    """
    The product vendor that created the device.
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
