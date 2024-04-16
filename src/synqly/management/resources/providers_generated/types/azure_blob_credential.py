# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...credentials.types.token_credential import TokenCredential
from ...credentials.types.token_credential_id import TokenCredentialId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AzureBlobCredential_Token(TokenCredential):
    type: typing.Literal["token"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AzureBlobCredential_TokenId(pydantic.BaseModel):
    type: typing.Literal["token_id"]
    value: TokenCredentialId

    class Config:
        frozen = True
        smart_union = True


AzureBlobCredential = typing.Union[AzureBlobCredential_Token, AzureBlobCredential_TokenId]
