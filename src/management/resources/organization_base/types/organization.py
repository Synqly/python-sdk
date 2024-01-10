# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...common.types.base import Base
from ...token_base.types.token_id import TokenId
from .organization_id import OrganizationId
from .organization_options import OrganizationOptions

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Organization(Base):
    id: OrganizationId
    refresh_token_id: TokenId = pydantic.Field(description="Organization refresh token id")
    fullname: str = pydantic.Field(description="Human friendly display name for this Organization")
    contact: str = pydantic.Field(description="Organization email address")
    reply_to: str = pydantic.Field(
        description="Reply-to email address, used for SMTP emails. Defaults to no-reply@synqly.com"
    )
    picture: str = pydantic.Field(description="URL of the organization")
    options: typing.Optional[OrganizationOptions] = pydantic.Field(description="Organization options")

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
