# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from .database_type_id import DatabaseTypeId
from .group import Group

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Database(pydantic.BaseModel):
    """
    The database object is used for databases which are typically datastore services that contain an organized collection of structured and unstructured data or a types of data.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the database was known to have been created.
    """

    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the database was known to have been created.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the database.
    """

    groups: typing.Optional[typing.List[Group]] = pydantic.Field(default=None)
    """
    The group names to which the database belongs.
    """

    modified_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The most recent time when any changes, updates, or modifications were made within the database.
    """

    modified_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The most recent time when any changes, updates, or modifications were made within the database.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The database name, ordinarily as assigned by a database administrator.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the database in bytes.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The database type.
    """

    type_id: DatabaseTypeId = pydantic.Field()
    """
    The normalized identifier of the database type.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the database.
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
