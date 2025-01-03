# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...credentials.types.bridge_basic_credential import BridgeBasicCredential
from ...credentials.types.bridge_basic_credential_id import BridgeBasicCredentialId
from ...credentials.types.bridge_o_auth_client_credential import BridgeOAuthClientCredential
from ...credentials.types.bridge_o_auth_client_credential_id import BridgeOAuthClientCredentialId
from ...credentials.types.bridge_token_credential import BridgeTokenCredential
from ...credentials.types.bridge_token_credential_id import BridgeTokenCredentialId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ElasticsearchBridgeCredentials_BridgeBasic(BridgeBasicCredential):
    type: typing.Literal["bridge_basic"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ElasticsearchBridgeCredentials_BridgeBasicId(pydantic.BaseModel):
    type: typing.Literal["bridge_basic_id"]
    value: BridgeBasicCredentialId

    class Config:
        frozen = True
        smart_union = True


class ElasticsearchBridgeCredentials_BridgeOAuthClient(BridgeOAuthClientCredential):
    type: typing.Literal["bridge_o_auth_client"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ElasticsearchBridgeCredentials_BridgeOAuthClientId(pydantic.BaseModel):
    type: typing.Literal["bridge_o_auth_client_id"]
    value: BridgeOAuthClientCredentialId

    class Config:
        frozen = True
        smart_union = True


class ElasticsearchBridgeCredentials_BridgeToken(BridgeTokenCredential):
    type: typing.Literal["bridge_token"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ElasticsearchBridgeCredentials_BridgeTokenId(pydantic.BaseModel):
    type: typing.Literal["bridge_token_id"]
    value: BridgeTokenCredentialId

    class Config:
        frozen = True
        smart_union = True


ElasticsearchBridgeCredentials = typing.Union[
    ElasticsearchBridgeCredentials_BridgeBasic,
    ElasticsearchBridgeCredentials_BridgeBasicId,
    ElasticsearchBridgeCredentials_BridgeOAuthClient,
    ElasticsearchBridgeCredentials_BridgeOAuthClientId,
    ElasticsearchBridgeCredentials_BridgeToken,
    ElasticsearchBridgeCredentials_BridgeTokenId,
]
