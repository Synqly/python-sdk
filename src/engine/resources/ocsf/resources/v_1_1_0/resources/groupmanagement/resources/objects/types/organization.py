# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Organization(pydantic.BaseModel):
    """
    The Organization object describes characteristics of an organization or company and its division if any.
    """

    name: typing.Optional[str] = pydantic.Field(description="The name of the organization. For example, Widget, Inc.")
    ou_name: typing.Optional[str] = pydantic.Field(
        description="The name of the organizational unit, within an organization. For example, Finance, IT, R&D"
    )
    ou_uid: typing.Optional[str] = pydantic.Field(
        description="The alternate identifier for an entity's unique identifier. For example, its Active Directory OU DN or AWS OU ID."
    )
    uid: typing.Optional[str] = pydantic.Field(
        description="The unique identifier of the organization. For example, its Active Directory or AWS Org ID."
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
