# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime
from .display import Display
from .keyboard_info import KeyboardInfo


class DeviceHwInfo(pydantic.BaseModel):
    """
    The Device Hardware Information object contains details and specifications of the physical components that make up a device. This information provides an overview of the hardware capabilities, configuration, and characteristics of the device.
    """

    bios_date: typing.Optional[str] = pydantic.Field(description="The BIOS date. For example: <code>03/31/16</code>.")
    bios_manufacturer: typing.Optional[str] = pydantic.Field(
        description="The BIOS manufacturer. For example: <code>LENOVO</code>."
    )
    bios_ver: typing.Optional[str] = pydantic.Field(
        description="The BIOS version. For example: <code>LENOVO G5ETA2WW (2.62)</code>."
    )
    chassis: typing.Optional[str] = pydantic.Field(
        description="The chassis type describes the system enclosure or physical form factor. Such as the following examples for Windows <a target='_blank' href='https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-systemenclosure'>Windows Chassis Types</a>"
    )
    cpu_bits: typing.Optional[int] = pydantic.Field(
        description="The cpu architecture, the number of bits used for addressing in memory. For example: <code>32</code> or <code>64</code>."
    )
    cpu_cores: typing.Optional[int] = pydantic.Field(
        description="The number of processor cores in all installed processors. For Example: <code>42</code>."
    )
    cpu_count: typing.Optional[int] = pydantic.Field(
        description="The number of physical processors on a system. For example: <code>1</code>."
    )
    cpu_speed: typing.Optional[int] = pydantic.Field(
        description="The speed of the processor in Mhz. For Example: <code>4200</code>."
    )
    cpu_type: typing.Optional[str] = pydantic.Field(
        description="The processor type. For example: <code>x86 Family 6 Model 37 Stepping 5</code>."
    )
    desktop_display: typing.Optional[Display] = pydantic.Field(
        description="The desktop display affiliated with the event"
    )
    keyboard_info: typing.Optional[KeyboardInfo] = pydantic.Field(description="The keyboard detailed information.")
    ram_size: typing.Optional[int] = pydantic.Field(
        description="The total amount of installed RAM, in Megabytes. For example: <code>2048</code>."
    )
    serial_number: typing.Optional[str] = pydantic.Field(description="The device manufacturer serial number.")

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
