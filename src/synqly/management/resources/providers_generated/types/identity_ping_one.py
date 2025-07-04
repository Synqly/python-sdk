# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .ping_one_credential import PingOneCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class IdentityPingOne(pydantic.BaseModel):
    """
    Configuration for PingOne Cloud Platform.

    [Configuration guide](https://docs.synqly.com/guides/provider-configuration/ping-identity-setup)
    """

    auth_url: str = pydantic.Field()
    """
    Base URL for making authentication requests to PingOne.
    """

    client_id: str = pydantic.Field()
    """
    Client ID for the application set up as a worker.
    """

    credential: PingOneCredential
    organization_id: str = pydantic.Field()
    """
    The organization ID that the client app is a part of.
    """

    url: str = pydantic.Field()
    """
    Base URL for the PingOne API.
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
