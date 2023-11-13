# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...common.types.base import Base
from ...common.types.id import Id
from ...token_base.types.token_id import TokenId
from ...token_base.types.token_pair import TokenPair


class RefreshToken(Base):
    id: TokenId
    member_id: typing.Optional[Id] = pydantic.Field(alias="memberId", description="Member Id")
    expires: dt.datetime = pydantic.Field(description="Time when this token expires and can no longer be used again.")
    token_ttl: str = pydantic.Field(alias="tokenTtl", description="Token time-to-live")
    primary: TokenPair = pydantic.Field(description="Primary running access and refresh tokens")
    secondary: TokenPair = pydantic.Field(
        description="Temporary secondary TokenPair created after a RefreshToken operation"
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
