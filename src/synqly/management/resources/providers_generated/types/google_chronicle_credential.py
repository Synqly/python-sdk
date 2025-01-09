# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...credentials.types.o_auth_client_credential import OAuthClientCredential
from ...credentials.types.o_auth_client_credential_id import OAuthClientCredentialId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GoogleChronicleCredential_OAuthClient(OAuthClientCredential):
    type: typing.Literal["o_auth_client"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GoogleChronicleCredential_OAuthClientId(pydantic.BaseModel):
    type: typing.Literal["o_auth_client_id"]
    value: OAuthClientCredentialId

    class Config:
        frozen = True
        smart_union = True


GoogleChronicleCredential = typing.Union[GoogleChronicleCredential_OAuthClient, GoogleChronicleCredential_OAuthClientId]
