# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...credentials.types.basic_credential import BasicCredential
from ...credentials.types.basic_credential_id import BasicCredentialId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NozomiVantageCredential_Basic(BasicCredential):
    type: typing.Literal["basic"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class NozomiVantageCredential_BasicId(pydantic.BaseModel):
    type: typing.Literal["basic_id"]
    value: BasicCredentialId

    class Config:
        frozen = True
        smart_union = True


NozomiVantageCredential = typing.Union[NozomiVantageCredential_Basic, NozomiVantageCredential_BasicId]
