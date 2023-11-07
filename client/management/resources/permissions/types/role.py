# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .action import Action
from .blocked_api import BlockedApi
from .object import Object


class Role(pydantic.BaseModel):
    actions: typing.List[Action] = pydantic.Field(
        description='List of actions that this permission grants access to: "create", "read", "update", "delete" and "*". Use "*" to give all action permissions.'
    )
    objects: typing.List[Object] = pydantic.Field(
        description='List of contained objects ids that this permission grants access to. Use "*" to grant access to all contained objects.'
    )
    blocked_apis: typing.Optional[typing.List[BlockedApi]] = pydantic.Field(
        description="Optional list of APIs that this role blocks access to. Can be used to block access to select APIs like /v1/user, v1/tokens and /v1/credentials"
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
