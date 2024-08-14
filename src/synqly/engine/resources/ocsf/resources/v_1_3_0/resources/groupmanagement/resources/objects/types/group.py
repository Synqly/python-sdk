# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Group(pydantic.BaseModel):
    """
    The Group object represents a collection or association of entities, such as users, policies, or devices. It serves as a logical grouping mechanism to organize and manage entities with similar characteristics or permissions within a system or organization.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The group description.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The domain where the group is defined. For example: the LDAP or Active Directory domain.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The group name.
    """

    privileges: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The group privileges.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the group or account.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the group. For example, for Windows events this is the security identifier (SID) of the group.
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
