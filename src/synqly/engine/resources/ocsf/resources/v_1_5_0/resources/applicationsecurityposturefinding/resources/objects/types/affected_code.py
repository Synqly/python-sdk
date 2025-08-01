# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .file import File
from .remediation import Remediation
from .rule import Rule
from .user import User

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AffectedCode(pydantic.BaseModel):
    """
    The Affected Code object describes details about a code block identified as vulnerable.
    """

    end_column: typing.Optional[int] = pydantic.Field(default=None)
    """
    The column number of the last part of the assessed code identified as vulnerable.
    """

    end_line: typing.Optional[int] = pydantic.Field(default=None)
    """
    The line number of the last line of code block identified as vulnerable.
    """

    file: File = pydantic.Field()
    """
    Details about the file that contains the affected code block.
    """

    owner: typing.Optional[User] = pydantic.Field(default=None)
    """
    Details about the user that owns the affected file.
    """

    remediation: typing.Optional[Remediation] = pydantic.Field(default=None)
    """
    Describes the recommended remediation steps to address identified issue(s).
    """

    rule: typing.Optional[Rule] = pydantic.Field(default=None)
    """
    Details about the specific rule, e.g., those defined as part of a larger <code>policy</code>, that triggered the finding.
    """

    start_column: typing.Optional[int] = pydantic.Field(default=None)
    """
    The column number of the first part of the assessed code identified as vulnerable.
    """

    start_line: typing.Optional[int] = pydantic.Field(default=None)
    """
    The line number of the first line of code block identified as vulnerable.
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
