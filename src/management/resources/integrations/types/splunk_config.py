# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class SplunkConfig(pydantic.BaseModel):
    """
    Configuration specific to the Splunk Event Provider
    """

    skip_tls_verify: bool = pydantic.Field(
        description="If true, skips verification of the Splunk server's TLS certificate. Defaults to false."
    )
    index: typing.Optional[str] = pydantic.Field(
        description="Splunk index to send events to. If not provided, will use the default index for the Splunk collector."
    )
    source: typing.Optional[str] = pydantic.Field(
        description="Splunk source to send events to. If not provided, will use the default source for the Splunk collector."
    )
    source_type: typing.Optional[str] = pydantic.Field(
        description="Splunk source type to send events to. If not provided, will use the default source type for the Splunk collector."
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