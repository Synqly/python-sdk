# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .remediation import Remediation
from .rule import Rule

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CisBenchmarkResult(pydantic.BaseModel):
    """
    The CIS Benchmark Result object contains information as defined by the Center for Internet Security (<a target='_blank' href='https://www.cisecurity.org/cis-benchmarks/'>CIS</a>) benchmark result. CIS Benchmarks are a collection of best practices for securely configuring IT systems, software, networks, and cloud infrastructure.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The CIS benchmark description.
    """

    name: str = pydantic.Field()
    """
    The CIS benchmark name.
    """

    remediation: typing.Optional[Remediation] = pydantic.Field(default=None)
    """
    Describes the recommended remediation steps to address identified issue(s).
    """

    rule: typing.Optional[Rule] = pydantic.Field(default=None)
    """
    The CIS benchmark rule.
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
