# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...common.types.base import Base
from ...ticketing.types.priority import Priority
from .notification_id import NotificationId
from .notification_status import NotificationStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Notification(Base):
    """
    Notification object
    """

    id: NotificationId
    priority: Priority = pydantic.Field()
    """
    Notification priority
    """

    notification_status: NotificationStatus = pydantic.Field()
    """
    Notification status
    """

    project: str = pydantic.Field()
    """
    Notification project
    """

    status: str = pydantic.Field()
    """
    The current status of the notification.
    """

    description: str = pydantic.Field()
    """
    Notification description.
    """

    summary: str = pydantic.Field()
    """
    Notification summary.
    """

    issue_type: str = pydantic.Field()
    """
    The notification's type.
    """

    creator: str = pydantic.Field()
    """
    The user who created this notification.
    """

    assignee: str = pydantic.Field()
    """
    Who notification is assigned to.
    """

    contact: str = pydantic.Field()
    """
    The notification contact information.
    """

    tags: typing.List[str] = pydantic.Field()
    """
    Associate tags with Notification
    """

    reference: str = pydantic.Field()
    """
    External URL reference
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
        allow_population_by_field_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
