# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .webhook_item import WebhookItem

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class WebhookConfig(pydantic.BaseModel):
    provider_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key used by Synqly to verify incoming webhook payloads sent by the Provider. The format and requirements for this key is Provider specific:
    
    - **ServiceNow**: Webhook payload signing is not currently supported, so the integrity of incoming ServiceNow payloads cannot be verified.
    - **Jira**: Synqly does _not_ automatically configure Jira webhooks. A user with administrator privileges must configure the webhook, including the signing key. If this key is not specified, Synqly will _not_ validate incoming webhooks from Jira. It is strongly recommended that a key is specified and configured with Jira to ensure the integrity of incoming payloads.
    """

    items: typing.List[WebhookItem] = pydantic.Field()
    """
    List of webhooks for an integration. If the provider supports webhooks, they will be sent to the servers provided in this list.
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
