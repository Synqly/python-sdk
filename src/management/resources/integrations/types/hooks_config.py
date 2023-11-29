# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...credentials.types.credential_id import CredentialId
from ...transforms.types.transform_id import TransformId


class HooksConfig(pydantic.BaseModel):
    """
    Configuration for a Webhook Provider
    """

    credential_id: CredentialId
    endpoint: typing.Optional[str] = pydantic.Field(description="Endpoint used for connecting to the external service.")
    filter: typing.Optional[str] = pydantic.Field(description="Optional webhook filter specification")
    source_events: typing.List[str] = pydantic.Field(description="Events to hook or empty list for all events")
    source_secret: typing.Optional[CredentialId] = pydantic.Field(description="Webhook verification secret")
    target_secret: typing.Optional[CredentialId] = pydantic.Field(
        description="Add optional webhook secure hash for verification"
    )
    transforms: typing.Optional[typing.List[TransformId]] = pydantic.Field(
        description="Optional list of transformations used to modify the webhook responses."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
