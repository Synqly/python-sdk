# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Session(pydantic.BaseModel):
    """
    The Session object describes details about an authenticated session. e.g. Session Creation Time, Session Issuer. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:Session/'>d3f:Session</a>.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(description="The time when the session was created.")
    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(description="The time when the session was created.")
    credential_uid: typing.Optional[str] = pydantic.Field(
        description="The unique identifier of the user's credential. For example, AWS Access Key ID."
    )
    expiration_time: typing.Optional[Timestamp] = pydantic.Field(description="The session expiration time.")
    expiration_time_dt: typing.Optional[dt.datetime] = pydantic.Field(description="The session expiration time.")
    is_remote: typing.Optional[bool] = pydantic.Field(description="The indication of whether the session is remote.")
    issuer: typing.Optional[str] = pydantic.Field(description="The identifier of the session issuer.")
    uid: typing.Optional[str] = pydantic.Field(description="The unique identifier of the session.")
    uuid_: typing.Optional[str] = pydantic.Field(
        alias="uuid", description="The universally unique identifier of the session."
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
