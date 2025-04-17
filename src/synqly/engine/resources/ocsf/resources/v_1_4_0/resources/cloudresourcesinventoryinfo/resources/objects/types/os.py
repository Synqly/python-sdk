# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .os_type_id import OsTypeId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Os(pydantic.BaseModel):
    """
    The Operating System (OS) object describes characteristics of an OS, such as Linux or Windows.
    """

    build: typing.Optional[str] = pydantic.Field(default=None)
    """
    The operating system build number.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The operating system country code, as defined by the ISO 3166-1 standard (Alpha-2 code).<p><b>Note:</b> The two letter country code should be capitalized. For example: <code>US</code> or <code>CA</code>.</p>
    """

    cpe_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Common Platform Enumeration (CPE) name as described by (<a target='_blank' href='https://nvd.nist.gov/products/cpe'>NIST</a>) For example: <code>cpe:/a:apple:safari:16.2</code>.
    """

    cpu_bits: typing.Optional[int] = pydantic.Field(default=None)
    """
    The cpu architecture, the number of bits used for addressing in memory. For example: <code>32</code> or <code>64</code>.
    """

    edition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The operating system edition. For example: <code>Professional</code>.
    """

    kernel_release: typing.Optional[str] = pydantic.Field(default=None)
    """
    The kernel release of the operating system. On Unix-based systems, this is determined from the <code>uname -r</code> command output, for example "5.15.0-122-generic".
    """

    lang: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two letter lower case language codes, as defined by <a target='_blank' href='https://en.wikipedia.org/wiki/ISO_639-1'>ISO 639-1</a>. For example: <code>en</code> (English), <code>de</code> (German), or <code>fr</code> (French).
    """

    name: str = pydantic.Field()
    """
    The operating system name.
    """

    sp_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the latest Service Pack.
    """

    sp_ver: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version number of the latest Service Pack.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the operating system.
    """

    type_id: OsTypeId = pydantic.Field()
    """
    The type identifier of the operating system.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the OS running on the device that originated the event. For example: "Windows 10", "OS X 10.7", or "iOS 9".
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
