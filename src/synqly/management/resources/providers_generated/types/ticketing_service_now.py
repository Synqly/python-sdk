# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .custom_field_mapping import CustomFieldMapping
from .service_now_credential import ServiceNowCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TicketingServiceNow(pydantic.BaseModel):
    """
    Configuration for ServiceNow as a Ticketing Provider
    """

    credential: ServiceNowCredential
    custom_field_mappings: typing.Optional[typing.List[CustomFieldMapping]] = pydantic.Field(default=None)
    """
    Custom field mappings for this provider.
    """

    url: str = pydantic.Field()
    """
    URL for the ServiceNow API. This should be the base URL for the API, without any path components and must be HTTPS. For example, "https://tenant.service-now.com".
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
