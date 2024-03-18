# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.url_string import UrlString

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Cwe(pydantic.BaseModel):
    """
    The CWE object represents a weakness in a software system that can be exploited by a threat actor to perform an attack. The CWE object is based on the <a target='_blank' href='https://cwe.mitre.org/'>Common Weakness Enumeration (CWE)</a> catalog.
    """

    caption: typing.Optional[str] = pydantic.Field(default=None)
    """
    The caption assigned to the Common Weakness Enumeration unique identifier.
    """

    src_url: typing.Optional[UrlString] = pydantic.Field(default=None)
    """
    URL pointing to the CWE Specification. For more information see <a target='_blank' href='https://cwe.mitre.org/'>CWE.</a>
    """

    uid: str = pydantic.Field()
    """
    The Common Weakness Enumeration unique number assigned to a specific weakness. A CWE Identifier begins "CWE" followed by a sequence of digits that acts as a unique identifier. For example: <code>CWE-123</code>.
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
