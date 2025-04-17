# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EmailAuth(pydantic.BaseModel):
    """
    The Email Authentication object describes the Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) and Domain-based Message Authentication, Reporting and Conformance (DMARC) attributes of an email.
    """

    dkim: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DomainKeys Identified Mail (DKIM) status of the email.
    """

    dkim_domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DomainKeys Identified Mail (DKIM) signing domain of the email.
    """

    dkim_signature: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DomainKeys Identified Mail (DKIM) signature used by the sending/receiving system.
    """

    dmarc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Domain-based Message Authentication, Reporting and Conformance (DMARC) status of the email.
    """

    dmarc_override: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Domain-based Message Authentication, Reporting and Conformance (DMARC) override action.
    """

    dmarc_policy: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Domain-based Message Authentication, Reporting and Conformance (DMARC) policy status.
    """

    spf: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Sender Policy Framework (SPF) status of the email.
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
