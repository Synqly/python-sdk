# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class HttpResponse(pydantic.BaseModel):
    """
    The HTTP Response object contains detailed information about the response sent from a web server to the requester. It encompasses attributes and metadata that describe the response status, headers, body content, and other relevant information.
    """

    code: int = pydantic.Field()
    """
    The numeric code sent from the web server to the requester.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The request header that identifies the original <a target='_blank' href='https://www.iana.org/assignments/media-types/media-types.xhtml'>media type </a> of the resource (prior to any content encoding applied for sending).
    """

    latency: typing.Optional[int] = pydantic.Field(default=None)
    """
    TODO: The HTTP response latency. In seconds, milliseconds, etc.?
    """

    length: typing.Optional[int] = pydantic.Field(default=None)
    """
    The HTTP response length, in number of bytes.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the event, as defined by the event source.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The response status. For example: Kubernetes responseStatus.status.
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
