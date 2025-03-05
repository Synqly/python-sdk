# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...ticketing.types.priority import Priority

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateNotificationRequest(pydantic.BaseModel):
    """
    Notification object
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This field is deprecated and no longer used.
    """

    summary: str = pydantic.Field()
    """
    Notification summary.
    """

    priority: typing.Optional[Priority] = pydantic.Field(default=None)
    """
    Notification priority
    """

    project: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notification project
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the notification.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notification description.
    """

    issue_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The notification's type.
    """

    creator: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user who created this notification.
    """

    assignee: typing.Optional[str] = pydantic.Field(default=None)
    """
    Who notification is assigned to.
    """

    contact: typing.Optional[str] = pydantic.Field(default=None)
    """
    The notification contact information.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Associate tags with Notification
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
