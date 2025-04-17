# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.url_string import UrlString
from .auth_factor import AuthFactor
from .fingerprint import Fingerprint
from .idp_state_id import IdpStateId
from .scim import Scim
from .sso import Sso

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Idp(pydantic.BaseModel):
    """
    The Identity Provider object contains detailed information about a provider responsible for creating, maintaining, and managing identity information while offering authentication services to applications. An Identity Provider (IdP) serves as a trusted authority that verifies the identity of users and issues authentication tokens or assertions to enable secure access to applications or services.
    """

    auth_factors: typing.Optional[typing.List[AuthFactor]] = pydantic.Field(default=None)
    """
    The Authentication Factors object describes the different types of Multi-Factor Authentication (MFA) methods and/or devices supported by the Identity Provider.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The primary domain associated with the Identity Provider.
    """

    fingerprint: typing.Optional[Fingerprint] = pydantic.Field(default=None)
    """
    The fingerprint of the X.509 certificate used by the Identity Provider.
    """

    has_mfa: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The Identity Provider enforces Multi Factor Authentication (MFA).
    """

    issuer: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier (often a URL) used by the Identity Provider as its issuer.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the Identity Provider.
    """

    protocol_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The supported protocol of the Identity Provider. E.g., <code>SAML</code>, <code>OIDC</code>, or <code>OAuth2</code>.
    """

    scim: typing.Optional[Scim] = pydantic.Field(default=None)
    """
    The System for Cross-domain Identity Management (SCIM) resource object provides a structured set of attributes related to SCIM protocols used for identity provisioning and management across cloud-based platforms. It standardizes user and group provisioning details, enabling identity synchronization and lifecycle management with compatible Identity Providers (IdPs) and applications. SCIM is defined in <a target='_blank' href='https://datatracker.ietf.org/doc/html/rfc7643'>RFC-7634</a>
    """

    sso: typing.Optional[Sso] = pydantic.Field(default=None)
    """
    The Single Sign-On (SSO) object provides a structure for normalizing SSO attributes, configuration, and/or settings from Identity Providers.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The configuration state of the Identity Provider, normalized to the caption of the <code>state_id</code> value. In the case of <code>Other</code>, it is defined by the event source.
    """

    state_id: typing.Optional[IdpStateId] = pydantic.Field(default=None)
    """
    The normalized state ID of the Identity Provider to reflect its configuration or activation status.
    """

    tenant_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tenant ID associated with the Identity Provider.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Identity Provider.
    """

    url_string: typing.Optional[UrlString] = pydantic.Field(default=None)
    """
    The URL for accessing the configuration or metadata of the Identity Provider.
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
