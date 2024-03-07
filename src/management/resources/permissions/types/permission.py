# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...common.types.id import Id
from ...role_base.types.adhoc_role import AdhocRole
from ...role_base.types.role_name import RoleName
from .role import Role

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Permission(pydantic.BaseModel):
    roles: typing.List[Role] = pydantic.Field(
        description="deprecated: List of access roles. Authorization tries each role sequentially until one access role passes or they all fail"
    )
    role_binding: typing.List[RoleName] = pydantic.Field(description="Roles granted to this token.")
    adhoc_role: typing.Optional[AdhocRole] = pydantic.Field(description="Adhoc role granted to this token.")
    resource_id: Id = pydantic.Field(description="ID of the resource that this permission grants access to.")
    resource_type: str = pydantic.Field(
        description='Type of the resource that this permission grants access to. Must be one of the following: "organization, "integration"'
    )
    parent_id: Id = pydantic.Field(description="Token parentId")
    id: Id = pydantic.Field(description="Token Id")
    organization_id: Id = pydantic.Field(description="Token organizationId")
    member_id: Id = pydantic.Field(description="Token memberId")

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
