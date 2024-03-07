# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.ip_address import IpAddress
from .http_header import HttpHeader
from .http_request_http_method import HttpRequestHttpMethod
from .url import Url

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class HttpRequest(pydantic.BaseModel):
    """
    The HTTP Request object represents the attributes of a request made to a web server. It encapsulates the details and metadata associated with an HTTP request, including the request method, headers, URL, query parameters, body content, and other relevant information.
    """

    args: typing.Optional[str] = pydantic.Field(description="The arguments sent along with the HTTP request.")
    http_headers: typing.Optional[typing.List[HttpHeader]] = pydantic.Field(
        description="Additional HTTP headers of an HTTP request or response."
    )
    http_method: typing.Optional[HttpRequestHttpMethod] = pydantic.Field(
        description="The <a target='_blank' href='https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods'>HTTP request method</a> indicates the desired action to be performed for a given resource."
    )
    length: typing.Optional[int] = pydantic.Field(description="The HTTP request length, in number of bytes.")
    referrer: typing.Optional[str] = pydantic.Field(
        description="The request header that identifies the address of the previous web page, which is linked to the current web page or resource being requested."
    )
    uid: typing.Optional[str] = pydantic.Field(description="The unique identifier of the http request.")
    url: typing.Optional[Url] = pydantic.Field(description="The URL object that pertains to the request.")
    user_agent: typing.Optional[str] = pydantic.Field(
        description="The request header that identifies the operating system and web browser."
    )
    version: typing.Optional[str] = pydantic.Field(description="The Hypertext Transfer Protocol (HTTP) version.")
    x_forwarded_for: typing.Optional[typing.List[IpAddress]] = pydantic.Field(
        description="The X-Forwarded-For header identifying the originating IP address(es) of a client connecting to a web server through an HTTP proxy or a load balancer."
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
