# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...member_base.types.create_member_request import CreateMemberRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateOrganizationRequest(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique short name for this Organization (lowercase [a-z0-9_-], can be used in URLs). Used for case insensitive duplicate name detection and default sort order. Defaults to OrganizationId if both name and fullname are not specified.
    """

    fullname: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human friendly display name for this Organization, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    """

    contact: str = pydantic.Field()
    """
    Organization email address
    """

    reply_to: str = pydantic.Field()
    """
    Reply-to email address, used for SMTP emails. Defaults to no-reply@synqly.com
    """

    picture: str = pydantic.Field()
    """
    URL of the organization
    """

    member: typing.Optional[CreateMemberRequest] = pydantic.Field(default=None)
    """
    Create organization member
    """

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
