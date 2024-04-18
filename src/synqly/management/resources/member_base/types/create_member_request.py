# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...role_base.types.role_name import RoleName
from .member_options import MemberOptions

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateMemberRequest(pydantic.BaseModel):
    name: str = pydantic.Field()
    """
    Email name to use for this Member. Also used for duplicate detection and default sort order.
    """

    fullname: typing.Optional[str] = pydantic.Field(default=None)
    """
    User's full display name. Defaults to the same value as the 'name' field if not specified.
    """

    nickname: typing.Optional[str] = pydantic.Field(default=None)
    """
    User's nickname
    """

    picture: typing.Optional[str] = pydantic.Field(default=None)
    """
    Url of user's picture
    """

    secret: str = pydantic.Field()
    """
    Member secret
    """

    role_binding: typing.Optional[typing.List[RoleName]] = pydantic.Field(default=None)
    """
    Roles granted to this member. Tokens inherit this access. Defaults to `member`.
    """

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
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}