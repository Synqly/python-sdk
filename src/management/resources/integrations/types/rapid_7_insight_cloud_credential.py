# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ...credentials.types.token_credential import TokenCredential
from ...credentials.types.token_credential_id import TokenCredentialId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Rapid7InsightCloudCredential_Token(TokenCredential):
    type: typing_extensions.Literal["token"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Rapid7InsightCloudCredential_TokenId(pydantic.BaseModel):
    type: typing_extensions.Literal["token_id"]
    value: TokenCredentialId

    class Config:
        frozen = True
        smart_union = True


Rapid7InsightCloudCredential = typing.Union[Rapid7InsightCloudCredential_Token, Rapid7InsightCloudCredential_TokenId]
