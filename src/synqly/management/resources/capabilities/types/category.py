# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...capabilities_base.types.category_id import CategoryId
from ...capabilities_base.types.provider_id import ProviderId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Category(pydantic.BaseModel):
    """
    Provides details on an available Integration.
    """

    category: CategoryId
    description: str = pydantic.Field()
    """
    Description of what this Integration does.
    """

    providers: typing.List[ProviderId] = pydantic.Field()
    """
    List of Providers that implement this Integration.
    """

    picture: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the icon representing this type of Integration.
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
