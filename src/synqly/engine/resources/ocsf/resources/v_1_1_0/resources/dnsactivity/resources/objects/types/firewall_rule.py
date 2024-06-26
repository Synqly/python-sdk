# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FirewallRule(pydantic.BaseModel):
    """
    The Firewall Rule object represents a specific rule within a firewall policy or event. It contains information about a rule's configuration, properties, and associated actions that define how network traffic is handled by the firewall.
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rule category.
    """

    condition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rule trigger condition for the rule. For example: SQL_INJECTION.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the rule that generated the event.
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The rule response time duration, usually used for challenge completion time.
    """

    match_details: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The data in a request that rule matched. For example: '["10","and","1"]'.
    """

    match_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location of the matched data in the source which resulted in the triggered firewall rule. For example: HEADER.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the rule that generated the event.
    """

    rate_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The rate limit for a rate-based rule.
    """

    sensitivity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sensitivity of the firewall rule in the matched event. For example: HIGH.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rule type.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the rule that generated the event.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rule version. For example: <code>1.1</code>.
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
