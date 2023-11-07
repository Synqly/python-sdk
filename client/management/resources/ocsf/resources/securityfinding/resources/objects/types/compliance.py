# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime


class Compliance(pydantic.BaseModel):
    """
    The Compliance object contains information about compliance requirements related of a finding generated by security tool.
    """

    requirements: typing.Optional[typing.List[str]] = pydantic.Field(
        description="A list of applicable compliance requirements for which this finding is related to."
    )
    status: typing.Optional[str] = pydantic.Field(
        description="The event status, normalized to the caption of the status_id value. In the case of 'Other', it is defined by the event source."
    )
    status_detail: typing.Optional[str] = pydantic.Field(
        description="The status details contains additional information about the event outcome."
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
