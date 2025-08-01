# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...engine.types.object import Object
from .note_id import NoteId
from .ticket_id import TicketId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Note(pydantic.BaseModel):
    """
    Note on a ticket
    """

    id: NoteId
    ticket_id: TicketId
    content: str = pydantic.Field()
    """
    The content of the note formatted as markdown.
    """

    creator: str = pydantic.Field()
    """
    The user who created the note.
    """

    title: str = pydantic.Field()
    """
    The title of the note.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date the comment was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the comment was last updated.
    """

    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Custom mapped fields for this note.
    """

    unmapped: typing.Optional[Object] = pydantic.Field(default=None)
    """
    The attributes that are not mapped to the comment schema. The names and values of those attributes are specific to the provider.
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
