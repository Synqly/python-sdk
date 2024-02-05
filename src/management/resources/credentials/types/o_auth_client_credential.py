# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OAuthClientCredential(pydantic.BaseModel):
    """
    A Client ID and secret used for authenticating with OAuth 2.0 compatible service using the client credentials grant.
    """

    token_url: str = pydantic.Field(description="The OAuth 2.0 token URL for the service provider")
    client_id: str = pydantic.Field(description="The ID of the client application defined at the service provider")
    client_secret: str = pydantic.Field(description="Secret value for authentication")
    extra: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="Optional connection specific meta data such as a signing key ID or organization ID"
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