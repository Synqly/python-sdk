# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .affected_package_type_id import AffectedPackageTypeId
from .fingerprint import Fingerprint
from .remediation import Remediation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AffectedPackage(pydantic.BaseModel):
    """
    The Affected Package object describes details about a software package identified as affected by a vulnerability/vulnerabilities.
    """

    architecture: typing.Optional[str] = pydantic.Field(default=None)
    """
    Architecture is a shorthand name describing the type of computer hardware the packaged software is meant to run on.
    """

    cpe_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Common Platform Enumeration (CPE) name for the software package.
    """

    epoch: typing.Optional[int] = pydantic.Field(default=None)
    """
    The software package epoch. Epoch is a way to define weighted dependencies based on version numbers.
    """

    fixed_in_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The software package version in which a reported vulnerability was patched/fixed.
    """

    hash: typing.Optional[Fingerprint] = pydantic.Field(default=None)
    """
    Cryptographic hash to identify the binary instance of a software component. This can include any component such file, package, or library.
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    The software license applied to this package.
    """

    name: str = pydantic.Field()
    """
    The software package name.
    """

    package_manager: typing.Optional[str] = pydantic.Field(default=None)
    """
    The software packager manager utilized to manage a package on a system, e.g. npm, yum, dpkg etc.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The installation path of the affected package.
    """

    purl: typing.Optional[str] = pydantic.Field(default=None)
    """
    A purl is a URL string used to identify and locate a software package in a mostly universal and uniform way across programming languages, package managers, packaging conventions, tools, APIs and databases.
    """

    release: typing.Optional[str] = pydantic.Field(default=None)
    """
    Release is the number of times a version of the software has been packaged.
    """

    remediation: typing.Optional[Remediation] = pydantic.Field(default=None)
    """
    Describes the recommended remediation steps to address identified issue(s).
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of software package, normalized to the caption of the type_id value. In the case of 'Other', it is defined by the source.
    """

    type_id: typing.Optional[AffectedPackageTypeId] = pydantic.Field(default=None)
    """
    The type of software package.
    """

    vendor_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the vendor who published the software package.
    """

    version: str = pydantic.Field()
    """
    The software package version.
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
