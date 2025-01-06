# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .slack_credential import SlackCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NotificationsSlack(pydantic.BaseModel):
    """
    Configuration for the Slack Notification Provider
    """

    channel: str = pydantic.Field()
    """
    The channel to send notifications to. Should be the ID of the desired channel.
    """

    credential: SlackCredential
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional URL override for the Slack API. This should include the full path to the API endpoint.
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
