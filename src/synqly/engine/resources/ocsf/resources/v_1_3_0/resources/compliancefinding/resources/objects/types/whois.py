# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.email_address import EmailAddress
from ...base.types.subnet import Subnet
from ...base.types.timestamp import Timestamp
from .autonomous_system import AutonomousSystem
from .domain_contact import DomainContact
from .whois_dnssec_status_id import WhoisDnssecStatusId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Whois(pydantic.BaseModel):
    """
    The resources of a WHOIS record for a given domain. This can include domain names, IP address blocks, autonomous system information, and/or contact and registration information for a domain.
    """

    autonomous_system: typing.Optional[AutonomousSystem] = pydantic.Field(default=None)
    """
    The autonomous system information associated with a domain.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    When the domain was registered or WHOIS entry was created.
    """

    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the domain was registered or WHOIS entry was created.
    """

    dnssec_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The normalized value of dnssec_status_id.
    """

    dnssec_status_id: typing.Optional[WhoisDnssecStatusId] = pydantic.Field(default=None)
    """
    Describes the normalized status of DNS Security Extensions (DNSSEC) for a domain.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the domain.
    """

    domain_contacts: typing.Optional[typing.List[DomainContact]] = pydantic.Field(default=None)
    """
    An array of <code>Domain Contact</code> objects.
    """

    email_addr: typing.Optional[EmailAddress] = pydantic.Field(default=None)
    """
    The email address for the registrar's abuse contact
    """

    last_seen_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    When the WHOIS record was last updated or seen at.
    """

    last_seen_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the WHOIS record was last updated or seen at.
    """

    name_servers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A collection of name servers related to a domain registration or other record.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number for the registrar's abuse contact
    """

    registrar: typing.Optional[str] = pydantic.Field(default=None)
    """
    The domain registrar.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of a domain and its ability to be transferred, e.g., <code>clientTransferProhibited</code>.
    """

    subdomains: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of subdomain strings. Can be used to collect several subdomains such as those from Domain Generation Algorithms (DGAs).
    """

    subnet: typing.Optional[Subnet] = pydantic.Field(default=None)
    """
    The IP address block (CIDR) associated with a domain.
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