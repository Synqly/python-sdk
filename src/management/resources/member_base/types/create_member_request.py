# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...permissions.types.role import Role
from ...role_base.types.role_name import RoleName
from .member_options import MemberOptions

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateMemberRequest(pydantic.BaseModel):
    name: str = pydantic.Field(
        description="Email name to use for this Member. Also used for duplicate detection and default sort order."
    )
    fullname: typing.Optional[str] = pydantic.Field(description="User's full display name")
    nickname: typing.Optional[str] = pydantic.Field(description="User's nickname")
    picture: typing.Optional[str] = pydantic.Field(description="Url of user's picture")
    secret: str = pydantic.Field(description="Member secret")
    roles: typing.List[Role] = pydantic.Field(
        description="Deprecated: Roles granted to this member. Tokens inherit this access."
    )
    role_binding: typing.List[RoleName] = pydantic.Field(
        description="Roles granted to this member. Tokens inherit this access."
    )
    options: MemberOptions

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
