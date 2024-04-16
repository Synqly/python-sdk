# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...credentials.types.secret_credential import SecretCredential
from ...credentials.types.secret_credential_id import SecretCredentialId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TeamsCredential_Secret(SecretCredential):
    type: typing.Literal["secret"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TeamsCredential_SecretId(pydantic.BaseModel):
    type: typing.Literal["secret_id"]
    value: SecretCredentialId

    class Config:
        frozen = True
        smart_union = True


TeamsCredential = typing.Union[TeamsCredential_Secret, TeamsCredential_SecretId]
