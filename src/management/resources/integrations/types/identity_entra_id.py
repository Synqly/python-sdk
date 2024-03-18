# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .entra_id_credential import EntraIdCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class IdentityEntraId(pydantic.BaseModel):
    """
    Configuration for the Microsoft Entra ID Identity Provider
    """

    credential: EntraIdCredential
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional URL override for the Microsoft Graph API. This should be the base URL for the API without any path components.
    """

    client_id: str = pydantic.Field()
    """
    Azure Client (Application) ID.
    """

    tenant_id: str = pydantic.Field()
    """
    Azure Directory (tenant) ID.
    """

    scopes: typing.List[str] = pydantic.Field()
    """
    Any custom scopes. Defaults to the primary microsoft graph API default scope.
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
