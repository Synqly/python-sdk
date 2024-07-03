# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...common.types.base_resource_request import BaseResourceRequest
from .priority import Priority
from .status import Status

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateTicketRequest(BaseResourceRequest):
    summary: str = pydantic.Field()
    """
    Ticket summary.
    """

    creator: typing.Optional[str] = pydantic.Field(default=None)
    """
    User who created this ticket.
    """

    assignee: typing.Optional[str] = pydantic.Field(default=None)
    """
    Who ticket is assigned to.
    """

    contact: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ticket contact information.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ticket description.
    """

    priority: typing.Optional[Priority] = pydantic.Field(default=None)
    """
    The priority of the Ticket
    """

    due_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The ticket's due date.
    """

    completion_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The ticket's complete date.
    """

    status: typing.Optional[Status] = pydantic.Field(default=None)
    """
    The current status of the ticket.
    """

    project: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket project.
    """

    issue_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket's type.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Associate tags with Ticket
    """

    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Set custom fields for this ticket, keys are the custom field names.
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
