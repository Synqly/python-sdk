# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...common.types.id import Id
from ...role_base.types.adhoc_role import AdhocRole
from ...role_base.types.role_name import RoleName

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Permission(pydantic.BaseModel):
    role_binding: typing.Optional[typing.List[RoleName]] = pydantic.Field(default=None)
    """
    Roles granted to this token.
    """

    adhoc_role: typing.Optional[AdhocRole] = pydantic.Field(default=None)
    """
    Adhoc role granted to this token.
    """

    resource_id: Id = pydantic.Field()
    """
    ID of the resource that this permission grants access to.
    """

    resource_type: str = pydantic.Field()
    """
    Type of the resource that this permission grants access to. Must be one of the following: "organization, "integration"
    """

    parent_id: Id = pydantic.Field()
    """
    Token parentId
    """

    id: Id = pydantic.Field()
    """
    Token Id
    """

    organization_id: Id = pydantic.Field()
    """
    Token organizationId
    """

    root_organization_id: typing.Optional[Id] = pydantic.Field(default=None)
    """
    Token root organizationId
    """

    member_id: Id = pydantic.Field()
    """
    Token memberId
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
