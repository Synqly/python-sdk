# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .aws_credential import AwsCredential
from .basic_credential import BasicCredential
from .o_auth_client_credential import OAuthClientCredential
from .secret_credential import SecretCredential
from .token_credential import TokenCredential


class CredentialConfig_Aws(AwsCredential):
    type: typing.Literal["aws"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class CredentialConfig_Token(TokenCredential):
    type: typing.Literal["token"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class CredentialConfig_Basic(BasicCredential):
    type: typing.Literal["basic"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class CredentialConfig_Secret(SecretCredential):
    type: typing.Literal["secret"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class CredentialConfig_OAuthClient(OAuthClientCredential):
    type: typing.Literal["o_auth_client"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


CredentialConfig = typing.Union[
    CredentialConfig_Aws,
    CredentialConfig_Token,
    CredentialConfig_Basic,
    CredentialConfig_Secret,
    CredentialConfig_OAuthClient,
]
