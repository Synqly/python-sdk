# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .problematic_parameter import ProblematicParameter
from .resource_reference import ResourceReference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProblemContext(pydantic.BaseModel):
    parameter: typing.Optional[ProblematicParameter] = pydantic.Field(default=None)
    """
    If the problem is related to a `query`, `header`, `path` or `body` parameter, this field will describe the problematic parameter and where to find it.
    """

    resources: typing.Optional[typing.List[ResourceReference]] = None
    raw_error: typing.Optional[str] = pydantic.Field(default=None)
    """
    If available this represents the underlying raw error, for example an error response from a Provider.
    """

    provider_details: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    If available this represents the underlying details from the provider. May include the error message, status code, and other details.
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
