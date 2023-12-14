# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ........core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Display(pydantic.BaseModel):
    """
    The Display object contains information about the physical or virtual display connected to a computer system.
    """

    color_depth: typing.Optional[int] = pydantic.Field(description="The numeric color depth.")
    physical_height: typing.Optional[int] = pydantic.Field(description="The numeric physical height of display.")
    physical_orientation: typing.Optional[int] = pydantic.Field(
        description="The numeric physical orientation of display."
    )
    physical_width: typing.Optional[int] = pydantic.Field(description="The numeric physical width of display.")
    scale_factor: typing.Optional[int] = pydantic.Field(description="The numeric scale factor of display.")

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
