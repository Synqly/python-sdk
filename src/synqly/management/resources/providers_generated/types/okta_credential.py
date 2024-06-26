# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...credentials.types.o_auth_client_credential import OAuthClientCredential
from ...credentials.types.o_auth_client_credential_id import OAuthClientCredentialId
from ...credentials.types.token_credential import TokenCredential
from ...credentials.types.token_credential_id import TokenCredentialId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OktaCredential_OAuthClient(OAuthClientCredential):
    type: typing.Literal["o_auth_client"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class OktaCredential_OAuthClientId(pydantic.BaseModel):
    type: typing.Literal["o_auth_client_id"]
    value: OAuthClientCredentialId

    class Config:
        frozen = True
        smart_union = True


class OktaCredential_Token(TokenCredential):
    type: typing.Literal["token"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class OktaCredential_TokenId(pydantic.BaseModel):
    type: typing.Literal["token_id"]
    value: TokenCredentialId

    class Config:
        frozen = True
        smart_union = True


OktaCredential = typing.Union[
    OktaCredential_OAuthClient, OktaCredential_OAuthClientId, OktaCredential_Token, OktaCredential_TokenId
]
