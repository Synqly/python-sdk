# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...capabilities.types.category_id import CategoryId
from ...capabilities.types.provider_id import ProviderId
from .provider_config import ProviderConfig


class CreateIntegrationRequest(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        description="Unique short name for this Integrations (lowercase [a-z0-9_-], can be used in URLs). Also used for case insenitive duplicate name detection and default sort order. Defaults to IntegrationId if both name and fullname are not specified."
    )
    fullname: typing.Optional[str] = pydantic.Field(
        description="Human friendly display name for this Integrations, will auto-generate 'name' field (if 'name' is not specified)"
    )
    category: CategoryId
    provider_type: ProviderId = pydantic.Field(description="Provider implementation to use for this Integration.")
    provider_config: typing.Optional[ProviderConfig] = pydantic.Field(
        description="Custom configuration for the Provider."
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
