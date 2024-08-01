# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...common.types.object import Object
from .attachment_id import AttachmentId
from .ticket_id import TicketId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AttachmentMetadata(pydantic.BaseModel):
    """
    Attachment in a ticketing system
    """

    id: AttachmentId = pydantic.Field()
    """
    Unique identifier for this attachment.
    """

    ticket_id: TicketId = pydantic.Field()
    """
    The ticket this attachment is associated with.
    """

    file_name: str = pydantic.Field()
    """
    The name of the file.
    """

    file_type: str = pydantic.Field()
    """
    The type of the file.
    """

    file_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the file in bytes.
    """

    created_date: dt.datetime = pydantic.Field()
    """
    The date the attachment was created.
    """

    creator: str = pydantic.Field()
    """
    The user who created the attachment.
    """

    unmapped: typing.Optional[Object] = pydantic.Field(default=None)
    """
    The attributes that are not mapped to the attachment metadata schema. The names and values of those attributes are specific to the provider.
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
