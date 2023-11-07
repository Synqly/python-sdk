# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...common.types.base import Base
from ...permissions.types.role import Role
from .member_id import MemberId
from .state import State


class Member(Base):
    id: MemberId
    state: State
    last_logon: dt.datetime = pydantic.Field(description="Last logon time")
    fullname: str = pydantic.Field(description="User's full name")
    nickname: str = pydantic.Field(description="User's nickname")
    picture: str = pydantic.Field(description="Url of user's picture")
    ttl: str
    token_ttl: str
    expires: dt.datetime
    roles: typing.List[Role] = pydantic.Field(description="Roles granted to this member. Tokens inherit this access.")

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
