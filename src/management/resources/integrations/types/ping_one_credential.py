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


class PingOneCredential_Token(TokenCredential):
    type: typing_extensions.Literal["token"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PingOneCredential_TokenId(pydantic.BaseModel):
    type: typing_extensions.Literal["token_id"]
    value: TokenCredentialId

    class Config:
        frozen = True
        smart_union = True


PingOneCredential = typing.Union[PingOneCredential_Token, PingOneCredential_TokenId]
