# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...providers_generated.types.provider_config_id import ProviderConfigId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class IntegrationEnvironments(pydantic.BaseModel):
    test: typing.Optional[typing.List[ProviderConfigId]] = pydantic.Field(default=None)
    """
    List of allowed providers for test environment.
    """

    prod: typing.Optional[typing.List[ProviderConfigId]] = pydantic.Field(default=None)
    """
    List of allowed providers for production environment.
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
