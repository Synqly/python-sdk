# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OrganizationOptions(pydantic.BaseModel):
    invite_duration: typing.Optional[str] = pydantic.Field(
        description="Duration new member invitations will be valid. Default: 168h (7 days), minimum 24h, maximum 168h (7 days)."
    )
    forgot_duration: typing.Optional[str] = pydantic.Field(
        description="Duration forgotten password invitations will be valid. Default: 24h, minimum 24h, maximum 168h (7 days)."
    )
    password_duration: typing.Optional[str] = pydantic.Field(
        description="Duration before member password expires, part of required password rotation. Default: 4320h (180 days), minimum: 24h, maximum: 8760h (365 days)."
    )
    minimum_password_length: typing.Optional[int] = pydantic.Field(
        description="Minimum password length. Default: 8, minimum 8, maximum 72."
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